import os

import streamlit as st


def _get_secret(section: str, key: str, default=None):
    try:
        return st.secrets.get(section, {}).get(key, default)
    except Exception:
        return default


def get_mysql_config() -> dict:
    ssl_required = _get_secret(
        "mysql",
        "ssl_required",
        os.getenv("MYSQL_SSL_REQUIRED", "false"),
    )
    if isinstance(ssl_required, str):
        ssl_required = ssl_required.lower() in {"1", "true", "yes", "required"}

    return {
        "host": _get_secret("mysql", "host", os.getenv("MYSQL_HOST", "localhost")),
        "port": int(_get_secret("mysql", "port", os.getenv("MYSQL_PORT", 3306))),
        "database": _get_secret("mysql", "database", os.getenv("MYSQL_DATABASE", "tam_bebeong")),
        "user": _get_secret("mysql", "user", os.getenv("MYSQL_USER", "root")),
        "password": _get_secret("mysql", "password", os.getenv("MYSQL_PASSWORD", "")),
        "ssl_required": bool(ssl_required),
    }


def get_default_admin() -> dict:
    return {
        "username": _get_secret("admin", "username", os.getenv("ADMIN_USERNAME", "admin")),
        "password": _get_secret("admin", "password", os.getenv("ADMIN_PASSWORD", "admin123")),
        "full_name": _get_secret("admin", "full_name", os.getenv("ADMIN_FULL_NAME", "Administrator")),
    }
