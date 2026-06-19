import streamlit as st

from src.config import get_default_admin
from src.constants import EDUCATION_OPTIONS, LIKERT_OPTIONS, QUESTION_GROUPS
from src.db import check_database_connection, init_database
from src.repositories.survey_repository import create_submission
from src.utils.auth import initialize_auth_state, login, logout
from src.utils.ui import (
    apply_responsive_styles,
    render_database_error,
    render_public_footer,
    render_public_header,
)


st.set_page_config(
    page_title="Dashboard TAM BEBEONG",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

initialize_auth_state()
apply_responsive_styles(hide_page_navigation=True)
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

render_public_header()
st.markdown(
    """
    <section class="survey-intro">
        <strong>Petunjuk pengisian</strong><br>
        Isi data umum responden tanpa mencantumkan identitas pribadi, kemudian pilih satu jawaban pada setiap pernyataan.
        Skala jawaban adalah 1 (Sangat Tidak Setuju) sampai 5 (Sangat Setuju).
        Mohon kuesioner diisi satu kali oleh setiap responden.
        Waktu pengisian diperkirakan 5-7 menit.
    </section>
    """,
    unsafe_allow_html=True,
)

if st.session_state["questionnaire_submitted"]:
    st.success(
        "Jawaban Anda sudah berhasil disimpan. Terima kasih atas partisipasinya."
    )
    render_public_footer()
    st.stop()

with st.form("asn_questionnaire_form"):
    st.subheader("Data Umum Responden")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Jenis kelamin", ["Laki-laki", "Perempuan"])
        age = st.number_input("Usia", min_value=18, max_value=65, value=30)
        education = st.selectbox("Pendidikan terakhir", EDUCATION_OPTIONS)
    with col2:
        work_unit = st.text_input("Unit kerja")
        position_name = st.text_input("Jabatan")
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
                index=None,
                key=question_code,
            )

    st.markdown(
        """
        <div class="privacy-note">
            Kuesioner ini tidak meminta nama, NIP, email, atau identitas pribadi lainnya.
            Data yang diberikan digunakan khusus untuk kepentingan penelitian dan
            evaluasi penerimaan layanan Aplikasi BEBEONG Banjar Super Apps.
        </div>
        """,
        unsafe_allow_html=True,
    )
    consent = st.checkbox(
        "Saya telah membaca penjelasan di atas dan bersedia menjadi responden penelitian ini."
    )
    submitted = st.form_submit_button("Kirim Kuesioner", type="primary")

    if submitted:
        required_fields = [work_unit, position_name]
        if not all(field.strip() for field in required_fields):
            st.error("Unit kerja dan jabatan wajib diisi.")
        elif any(answer is None for answer in answers.values()):
            st.error("Seluruh pertanyaan kuesioner wajib dijawab.")
        elif not consent:
            st.error("Persetujuan responden wajib dicentang sebelum kuesioner dikirim.")
        else:
            respondent = {
                "gender": gender,
                "age": int(age),
                "work_unit": work_unit.strip(),
                "position_name": position_name.strip(),
                "education": education,
                "years_of_service": int(years_of_service),
            }
            create_submission(respondent, answers)
            st.session_state["questionnaire_submitted"] = True
            st.rerun()

render_public_footer()

