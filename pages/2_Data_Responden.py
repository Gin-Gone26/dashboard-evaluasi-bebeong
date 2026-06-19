import streamlit as st

from src.constants import EDUCATION_OPTIONS
from src.db import init_database
from src.repositories.survey_repository import delete_respondent, get_respondents, update_respondent
from src.services.export_service import dataframe_to_csv_bytes, dataframe_to_excel_bytes
from src.utils.auth import render_admin_sidebar, require_admin
from src.utils.ui import apply_responsive_styles, render_admin_note, render_admin_page_header, render_database_error, render_filters


st.set_page_config(page_title="Data Responden", page_icon="👥", layout="wide")
apply_responsive_styles()

try:
    init_database()
except Exception as exc:
    render_database_error(str(exc))
    st.stop()

require_admin()
render_admin_sidebar()

render_admin_page_header(
    "Data Responden",
    "Kelola data umum responden yang telah mengisi kuesioner TAM. Halaman ini tidak menyimpan nama, NIP, email, atau identitas pribadi responden.",
)
filters = render_filters("respondents")
data = get_respondents(filters)

st.subheader("Export Data Responden")
col1, col2 = st.columns(2)
with col1:
    st.download_button(
        "Download CSV Responden",
        dataframe_to_csv_bytes(data),
        file_name="data_responden_tam_bebeong.csv",
        mime="text/csv",
        disabled=data.empty,
    )
with col2:
    st.download_button(
        "Download Excel Responden",
        dataframe_to_excel_bytes(data, "Responden"),
        file_name="data_responden_tam_bebeong.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        disabled=data.empty,
    )

st.subheader("Tabel Data Responden")
st.dataframe(data, use_container_width=True, hide_index=True)

st.subheader("Edit Data Responden")
if data.empty:
    st.info("Belum ada data responden.")
else:
    selected_id = st.selectbox(
        "Pilih responden",
        data["id"].tolist(),
        format_func=lambda value: f"Responden #{value}",
    )
    selected = data.loc[data["id"] == selected_id].iloc[0]
    with st.form("edit_respondent_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            gender = st.selectbox(
                "Jenis kelamin",
                ["Laki-laki", "Perempuan"],
                index=["Laki-laki", "Perempuan"].index(selected["gender"]),
            )
            age = st.number_input("Usia", min_value=18, max_value=65, value=int(selected["age"]))
            education = st.selectbox(
                "Pendidikan terakhir",
                EDUCATION_OPTIONS,
                index=EDUCATION_OPTIONS.index(selected["education"]) if selected["education"] in EDUCATION_OPTIONS else 0,
            )
        with col_b:
            work_unit = st.text_input("Unit kerja", value=selected["work_unit"])
            position_name = st.text_input("Jabatan", value=selected["position_name"])
            years_of_service = st.number_input(
                "Masa kerja (tahun)",
                min_value=0,
                max_value=45,
                value=int(selected["years_of_service"]),
            )
        save = st.form_submit_button("Simpan Perubahan")
        if save:
            update_respondent(
                int(selected_id),
                {
                    "gender": gender,
                    "age": int(age),
                    "work_unit": work_unit.strip(),
                    "position_name": position_name.strip(),
                    "education": education,
                    "years_of_service": int(years_of_service),
                },
            )
            st.success("Data responden berhasil diperbarui.")
            st.rerun()

    st.subheader("Hapus Data")
    render_admin_note("Menghapus responden juga akan menghapus jawaban kuesioner miliknya.", danger=True)
    if st.button("Hapus Responden Terpilih", type="secondary"):
        delete_respondent(int(selected_id))
        st.success("Data responden berhasil dihapus.")
        st.rerun()
