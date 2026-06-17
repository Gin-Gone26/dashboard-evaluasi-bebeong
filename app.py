import streamlit as st

from src.config import get_default_admin
from src.constants import EDUCATION_OPTIONS, LIKERT_OPTIONS, QUESTION_GROUPS
from src.db import check_database_connection, init_database
from src.repositories.survey_repository import DuplicateRespondentError, create_submission
from src.utils.auth import initialize_auth_state, login, logout
from src.utils.ui import apply_responsive_styles, render_database_error


st.set_page_config(
    page_title="Dashboard TAM Bebeong",
    page_icon="📊",
    layout="wide",
)

initialize_auth_state()
apply_responsive_styles()
st.session_state.setdefault("questionnaire_submitted", False)

try:
    init_database()
except Exception as exc:
    render_database_error(str(exc))
    st.stop()


def render_login_sidebar() -> None:
    st.sidebar.header("Admin")
    if st.session_state["is_admin_logged_in"]:
        admin = st.session_state["admin_user"]
        st.sidebar.success(f"Login sebagai {admin['full_name']}")
        st.sidebar.page_link("pages/1_Dashboard_Admin.py", label="Buka Dashboard Admin")
        if st.sidebar.button("Logout"):
            logout()
            st.rerun()
        return

    with st.sidebar.form("login_form"):
        username = st.text_input("Username", value=get_default_admin()["username"])
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            if login(username, password):
                st.success("Login berhasil.")
                st.rerun()
            else:
                st.error("Username atau password salah.")


render_login_sidebar()

ok, message = check_database_connection()
if not ok:
    render_database_error(message)
    st.stop()

st.title("Dashboard Evaluasi Penerimaan ASN terhadap Website Bebeong Kota Banjar")
st.caption("Metode Technology Acceptance Model (TAM): PEOU, PU, dan BI")

st.info(
    "Silakan isi biodata dan kuesioner berikut. Jawaban menggunakan skala 1 sampai 5, "
    "dari Sangat Tidak Setuju sampai Sangat Setuju."
)

if st.session_state["questionnaire_submitted"]:
    st.success(
        "Jawaban Anda sudah berhasil disimpan. Setiap ASN hanya dapat mengisi kuesioner satu kali."
    )
    st.stop()

with st.form("asn_questionnaire_form"):
    st.subheader("Biodata Responden")
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Nama lengkap")
        nip = st.text_input(
            "NIP",
            max_chars=18,
            help="Wajib diisi dengan 18 digit. NIP digunakan untuk mencegah pengisian berulang.",
        )
        gender = st.selectbox("Jenis kelamin", ["Laki-laki", "Perempuan"])
        age = st.number_input("Usia", min_value=18, max_value=65, value=30)
        email = st.text_input("Email", help="Opsional.")
    with col2:
        work_unit = st.text_input("Unit kerja")
        position_name = st.text_input("Jabatan")
        education = st.selectbox("Pendidikan terakhir", EDUCATION_OPTIONS)
        years_of_service = st.number_input("Masa kerja (tahun)", min_value=0, max_value=45, value=1)

    st.subheader("Kuesioner TAM")
    st.caption("1 = Sangat Tidak Setuju, 2 = Tidak Setuju, 3 = Netral, 4 = Setuju, 5 = Sangat Setuju")

    answers = {}
    for group_code, group in QUESTION_GROUPS.items():
        st.markdown(f"#### {group_code} - {group['label']}")
        for question_code, question_text in group["questions"].items():
            answers[question_code] = st.radio(
                f"{question_code}. {question_text}",
                options=list(LIKERT_OPTIONS.keys()),
                format_func=lambda value: LIKERT_OPTIONS[value],
                horizontal=True,
                key=question_code,
            )

    submitted = st.form_submit_button("Kirim Jawaban")

    if submitted:
        required_fields = [full_name, work_unit, position_name]
        if not all(field.strip() for field in required_fields):
            st.error("Nama lengkap, unit kerja, dan jabatan wajib diisi.")
        elif not nip.strip().isdigit() or len(nip.strip()) != 18:
            st.error("NIP wajib terdiri dari tepat 18 digit angka.")
        else:
            respondent = {
                "full_name": full_name.strip(),
                "nip": nip.strip(),
                "gender": gender,
                "age": int(age),
                "work_unit": work_unit.strip(),
                "position_name": position_name.strip(),
                "education": education,
                "years_of_service": int(years_of_service),
                "email": email.strip() or None,
            }
            try:
                create_submission(respondent, answers)
                st.session_state["questionnaire_submitted"] = True
                st.rerun()
            except DuplicateRespondentError:
                st.error(
                    "NIP tersebut sudah pernah mengisi kuesioner. "
                    "Setiap ASN hanya dapat mengirim satu jawaban."
                )
