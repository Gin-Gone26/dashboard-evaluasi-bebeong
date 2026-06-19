import streamlit as st

from src.db import init_database
from src.repositories.survey_repository import get_questionnaires, get_respondents
from src.services.export_service import build_report_html
from src.utils.auth import render_admin_sidebar, require_admin
from src.utils.ui import (
    apply_responsive_styles,
    render_admin_note,
    render_admin_page_header,
    render_database_error,
    render_variable_chart,
    variable_score_dataframe,
)


st.set_page_config(page_title="Laporan Evaluasi", page_icon="📄", layout="wide")
apply_responsive_styles()

try:
    init_database()
except Exception as exc:
    render_database_error(str(exc))
    st.stop()

require_admin()
render_admin_sidebar()

render_admin_page_header(
    "Laporan Evaluasi",
    "Ringkasan laporan evaluasi penerimaan ASN terhadap Website BEBEONG berdasarkan data yang telah terkumpul.",
)

respondents = get_respondents()
questionnaires = get_questionnaires()
scores = variable_score_dataframe(questionnaires)
summary = {
    "total_respondents": len(respondents),
    "total_questionnaires": len(questionnaires),
}

col1, col2 = st.columns(2)
col1.metric("Total Responden", summary["total_respondents"])
col2.metric("Total Jawaban Kuesioner", summary["total_questionnaires"])

render_admin_note(
    "Laporan ini memuat ringkasan data dari dashboard. Hasil analisis statistik lengkap dapat dilampirkan dari file Jamovi yang telah diunggah."
)

st.subheader("Rata-rata Variabel TAM")
st.dataframe(scores, use_container_width=True, hide_index=True)
render_variable_chart(scores)

st.subheader("Narasi Laporan")
st.write(
    "Dashboard ini menampilkan hasil pengumpulan data penerimaan ASN terhadap Website BEBEONG "
    "berdasarkan variabel TAM: Perceived Ease of Use, Perceived Usefulness, dan Behavioral Intention. "
    "Data yang ditampilkan dapat diekspor dan dianalisis lebih lanjut menggunakan Jamovi."
)

report_bytes = build_report_html(summary, scores)
st.download_button(
    "Download Laporan HTML",
    report_bytes,
    file_name="laporan_evaluasi_tam_bebeong.html",
    mime="text/html",
)
