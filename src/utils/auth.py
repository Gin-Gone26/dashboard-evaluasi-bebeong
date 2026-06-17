import streamlit as st

from src.repositories.admin_repository import get_admin_by_username
from src.security import verify_password


def initialize_auth_state() -> None:
    st.session_state.setdefault("is_admin_logged_in", False)
    st.session_state.setdefault("admin_user", None)


def login(username: str, password: str) -> bool:
    admin = get_admin_by_username(username)
    if admin and verify_password(password, admin["password_hash"]):
        st.session_state["is_admin_logged_in"] = True
        st.session_state["admin_user"] = {
            "id": admin["id"],
            "username": admin["username"],
            "full_name": admin["full_name"],
        }
        return True
    return False


def logout() -> None:
    st.session_state["is_admin_logged_in"] = False
    st.session_state["admin_user"] = None


def require_admin() -> None:
    initialize_auth_state()
    if not st.session_state["is_admin_logged_in"]:
        st.warning("Silakan login sebagai admin melalui halaman utama.")
        st.stop()


def render_admin_sidebar() -> None:
    initialize_auth_state()
    if st.session_state["is_admin_logged_in"]:
        admin = st.session_state["admin_user"]
        st.sidebar.success(f"Login sebagai {admin['full_name']}")
        if st.sidebar.button("Logout"):
            logout()
            st.rerun()
