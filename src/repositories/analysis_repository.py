import pandas as pd
from sqlalchemy import text

from src.db import get_engine


def save_jamovi_upload(title: str, description: str, uploaded_file, admin_id: int | None) -> None:
    with get_engine().begin() as conn:
        conn.execute(
            text(
                """
                INSERT INTO jamovi_uploads
                    (title, description, file_name, file_type, file_content, uploaded_by)
                VALUES
                    (:title, :description, :file_name, :file_type, :file_content, :uploaded_by)
                """
            ),
            {
                "title": title,
                "description": description,
                "file_name": uploaded_file.name,
                "file_type": uploaded_file.type or "application/octet-stream",
                "file_content": uploaded_file.getvalue(),
                "uploaded_by": admin_id,
            },
        )


def get_jamovi_uploads() -> pd.DataFrame:
    query = """
        SELECT
            j.id,
            j.title,
            j.description,
            j.file_name,
            j.file_type,
            OCTET_LENGTH(j.file_content) AS file_size,
            a.full_name AS uploaded_by,
            j.uploaded_at
        FROM jamovi_uploads j
        LEFT JOIN admins a ON a.id = j.uploaded_by
        ORDER BY j.uploaded_at DESC
    """
    return pd.read_sql(text(query), get_engine())


def get_jamovi_file(upload_id: int) -> dict | None:
    with get_engine().begin() as conn:
        row = conn.execute(
            text("SELECT file_name, file_type, file_content FROM jamovi_uploads WHERE id = :id"),
            {"id": upload_id},
        ).mappings().first()
        return dict(row) if row else None


def delete_jamovi_upload(upload_id: int) -> None:
    with get_engine().begin() as conn:
        conn.execute(text("DELETE FROM jamovi_uploads WHERE id = :id"), {"id": upload_id})
