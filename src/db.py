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
          full_name VARCHAR(120) NOT NULL,
          nip VARCHAR(30) NULL,
          gender ENUM('Laki-laki', 'Perempuan') NOT NULL,
          age INT NOT NULL,
          work_unit VARCHAR(150) NOT NULL,
          position_name VARCHAR(120) NOT NULL,
          education VARCHAR(50) NOT NULL,
          years_of_service INT NOT NULL,
          email VARCHAR(120) NULL,
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

    ensure_default_admin()
    ensure_unique_nip_constraint()


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


def ensure_unique_nip_constraint() -> None:
    engine = get_engine()
    with engine.begin() as conn:
        index_exists = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM information_schema.statistics
                WHERE table_schema = DATABASE()
                  AND table_name = 'respondents'
                  AND index_name = 'uq_respondents_nip'
                """
            )
        ).scalar_one()
        if index_exists:
            return

        duplicate_count = conn.execute(
            text(
                """
                SELECT COUNT(*)
                FROM (
                    SELECT nip
                    FROM respondents
                    WHERE nip IS NOT NULL AND nip <> ''
                    GROUP BY nip
                    HAVING COUNT(*) > 1
                ) duplicate_nips
                """
            )
        ).scalar_one()
        if duplicate_count == 0:
            conn.execute(
                text(
                    "CREATE UNIQUE INDEX uq_respondents_nip "
                    "ON respondents (nip)"
                )
            )


def check_database_connection() -> tuple[bool, str]:
    try:
        run_query("SELECT 1")
        return True, "Koneksi database berhasil."
    except SQLAlchemyError as exc:
        return False, str(exc)
