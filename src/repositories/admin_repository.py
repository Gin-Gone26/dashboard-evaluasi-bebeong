from sqlalchemy import text

from src.db import get_engine


def get_admin_by_username(username: str) -> dict | None:
    with get_engine().begin() as conn:
        row = conn.execute(
            text("SELECT id, username, password_hash, full_name FROM admins WHERE username = :username"),
            {"username": username},
        ).mappings().first()
        return dict(row) if row else None
