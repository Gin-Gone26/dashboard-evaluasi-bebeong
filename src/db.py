from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus

import streamlit as st

from src.config import get_default_admin, get_mysql_config
from src.security import hash_password


@st.cache_resource(show_spinner=False)
def get_engine() -> Engine:
    config = get_mysql_config()
    password = quote_plus(config["password"])
    user = quote_plus(config["user"])
    host = config["host"]
    port = config["port"]
    database = config["database"]
    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4"
    connect_args = {"ssl": {}} if config["ssl_required"] else {}
    return create_engine(
        url,
        connect_args=connect_args,
        pool_pre_ping=True,
        pool_recycle=3600,
    )


def run_query(query: str, params: dict | None = None):
    engine = get_engine()
    with engine.begin() as conn:
        return conn.execute(text(query), params or {})


def init_database() -> None:
    statements = [
        """
        CREATE TABLE IF NOT EXISTS admins (
          id INT AUTO_INCREMENT PRIMARY KEY,
          username VARCHAR(50) NOT NULL UNIQUE,
          password_hash VARCHAR(255) NOT NULL,
          full_name VARCHAR(100) NOT NULL DEFAULT 'Administrator',
          created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB
        """,
        """
        CREATE TABLE IF NOT EXISTS respondents (
          id INT AUTO_INCREMENT PRIMARY KEY,
          gender ENUM('Laki-laki', 'Perempuan') NOT NULL,
          age INT NOT NULL,
          work_unit VARCHAR(150) NOT NULL,
          position_name VARCHAR(120) NULL,
          education VARCHAR(50) NOT NULL,
          years_of_service INT NOT NULL,
          created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB
        """,
        """
        CREATE TABLE IF NOT EXISTS questionnaires (
          id INT AUTO_INCREMENT PRIMARY KEY,
          respondent_id INT NOT NULL,
          PEOU1 TINYINT NOT NULL, PEOU2 TINYINT NOT NULL, PEOU3 TINYINT NOT NULL,
          PEOU4 TINYINT NOT NULL, PEOU5 TINYINT NOT NULL, PEOU6 TINYINT NOT NULL,
          PEOU7 TINYINT NOT NULL, PU1 TINYINT NOT NULL, PU2 TINYINT NOT NULL,
          PU3 TINYINT NOT NULL, PU4 TINYINT NOT NULL, PU5 TINYINT NOT NULL,
          PU6 TINYINT NOT NULL, PU7 TINYINT NOT NULL, BI1 TINYINT NOT NULL,
          BI2 TINYINT NOT NULL, BI3 TINYINT NOT NULL, BI4 TINYINT NOT NULL,
          BI5 TINYINT NOT NULL, BI6 TINYINT NOT NULL,
          suggestion TEXT NULL,
          submitted_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          CONSTRAINT fk_questionnaires_respondents
            FOREIGN KEY (respondent_id) REFERENCES respondents(id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """,
        """
        CREATE TABLE IF NOT EXISTS jamovi_uploads (
          id INT AUTO_INCREMENT PRIMARY KEY,
          title VARCHAR(150) NOT NULL,
          description TEXT NULL,
          file_name VARCHAR(255) NOT NULL,
          file_type VARCHAR(100) NOT NULL,
          file_content LONGBLOB NOT NULL,
          uploaded_by INT NULL,
          uploaded_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          CONSTRAINT fk_jamovi_uploads_admins
            FOREIGN KEY (uploaded_by) REFERENCES admins(id)
            ON DELETE SET NULL
        ) ENGINE=InnoDB
        """,
    ]
    engine = get_engine()
    with engine.begin() as conn:
        for statement in statements:
            conn.execute(text(statement))

    migrate_private_respondent_columns()
    migrate_optional_position_and_suggestion()
    ensure_default_admin()


def ensure_default_admin() -> None:
    admin = get_default_admin()
    engine = get_engine()
    with engine.begin() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM admins")).scalar_one()
        if count == 0:
            conn.execute(
                text(
                    """
                    INSERT INTO admins (username, password_hash, full_name)
                    VALUES (:username, :password_hash, :full_name)
                    """
                ),
                {
                    "username": admin["username"],
                    "password_hash": hash_password(admin["password"]),
                    "full_name": admin["full_name"],
                },
            )


def _column_exists(conn, table_name: str, column_name: str) -> bool:
    return bool(
        conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM information_schema.columns
                WHERE table_schema = DATABASE()
                  AND table_name = :table_name
                  AND column_name = :column_name
                """
            ),
            {"table_name": table_name, "column_name": column_name},
        ).scalar_one()
    )


def _index_exists(conn, table_name: str, index_name: str) -> bool:
    return bool(
        conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM information_schema.statistics
                WHERE table_schema = DATABASE()
                  AND table_name = :table_name
                  AND index_name = :index_name
                """
            ),
            {"table_name": table_name, "index_name": index_name},
        ).scalar_one()
    )


def migrate_private_respondent_columns() -> None:
    """Remove respondent identity columns from older installations."""
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text("DROP VIEW IF EXISTS v_questionnaire_scores"))
        if _index_exists(conn, "respondents", "uq_respondents_nip"):
            conn.execute(text("DROP INDEX uq_respondents_nip ON respondents"))
        for column_name in ("full_name", "nip", "email"):
            if _column_exists(conn, "respondents", column_name):
                conn.execute(text(f"ALTER TABLE respondents DROP COLUMN {column_name}"))


def migrate_optional_position_and_suggestion() -> None:
    """Keep older databases compatible with the current anonymous questionnaire form."""
    engine = get_engine()
    with engine.begin() as conn:
        if _column_exists(conn, "respondents", "position_name"):
            conn.execute(text("ALTER TABLE respondents MODIFY position_name VARCHAR(120) NULL"))
        if not _column_exists(conn, "questionnaires", "suggestion"):
            conn.execute(text("ALTER TABLE questionnaires ADD COLUMN suggestion TEXT NULL AFTER BI6"))


def check_database_connection() -> tuple[bool, str]:
    try:
        run_query("SELECT 1")
        return True, "Koneksi database berhasil."
    except SQLAlchemyError as exc:
        return False, str(exc)
