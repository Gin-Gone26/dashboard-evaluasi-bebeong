import streamlit as st

from src.db import init_database
from src.repositories.survey_repository import get_questionnaires
from src.services.export_service import dataframe_to_csv_bytes, dataframe_to_excel_bytes
from src.utils.auth import render_admin_sidebar, require_admin
from src.utils.ui import (
    apply_responsive_styles,
    render_admin_note,
    render_admin_page_header,
    render_database_error,
    render_filters,
    render_variable_chart,
    variable_score_dataframe,
)


st.set_page_config(page_title="Hasil Kuesioner", page_icon="📝", layout="wide")
apply_responsive_styles()

try:
    init_database()
except Exception as exc:
    render_database_error(str(exc))
    st.stop()

require_admin()
render_admin_sidebar()

render_admin_page_header(
    "Hasil Kuesioner TAM",
    "Lihat jawaban skala Likert PU, PEOU, dan BI. File export dari halaman ini dapat digunakan sebagai bahan analisis lanjutan di Jamovi.",
)
filters = render_filters("questionnaires")
data = get_questionnaires(filters)
scores = variable_score_dataframe(data)

render_admin_note(
    "Dashboard hanya menampilkan ringkasan dan visualisasi deskriptif. Pengujian validitas, reliabilitas, dan regresi tetap dilakukan di Jamovi."
)

st.subheader("Export Data Kuesioner")
col1, col2 = st.columns(2)
with col1:
    st.download_button(
        "Download CSV untuk Jamovi",
        dataframe_to_csv_bytes(data),
        file_name="hasil_kuesioner_tam_bebeong.csv",
        mime="text/csv",
        disabled=data.empty,
    )
with col2:
    st.download_button(
        "Download Excel untuk Jamovi",
        dataframe_to_excel_bytes(data, "Kuesioner TAM"),
        file_name="hasil_kuesioner_tam_bebeong.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        disabled=data.empty,
    )

st.subheader("Ringkasan Rata-rata Variabel")
render_variable_chart(scores)

st.subheader("Tabel Hasil Kuesioner")
st.dataframe(data, use_container_width=True, hide_index=True)
