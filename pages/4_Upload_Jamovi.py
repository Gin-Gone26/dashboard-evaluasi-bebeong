import streamlit as st

from src.db import init_database
from src.repositories.analysis_repository import (
    delete_jamovi_upload,
    get_jamovi_file,
    get_jamovi_uploads,
    save_jamovi_upload,
)
from src.utils.auth import render_admin_sidebar, require_admin
from src.utils.ui import apply_responsive_styles, render_admin_note, render_admin_page_header, render_database_error


st.set_page_config(page_title="Upload Jamovi", page_icon="📎", layout="wide")
apply_responsive_styles()

try:
    init_database()
except Exception as exc:
    render_database_error(str(exc))
    st.stop()

require_admin()
render_admin_sidebar()

render_admin_page_header(
    "Upload Hasil Analisis Jamovi",
    "Simpan arsip hasil analisis dari Jamovi seperti file OMV, tabel export, PDF, HTML, atau dokumen pendukung laporan.",
)
render_admin_note(
    "File yang diunggah pada halaman ini berfungsi sebagai arsip. Grafik dashboard tetap berasal dari jawaban kuesioner yang tersimpan di database."
)

with st.form("upload_jamovi_form"):
    title = st.text_input("Judul hasil analisis")
    description = st.text_area("Catatan")
    uploaded_file = st.file_uploader(
        "Pilih file hasil analisis",
        type=["omv", "csv", "xlsx", "html", "pdf", "docx"],
    )
    submitted = st.form_submit_button("Simpan Upload")
    if submitted:
        if not title.strip() or uploaded_file is None:
            st.error("Judul dan file wajib diisi.")
        else:
            admin_id = st.session_state["admin_user"]["id"]
            save_jamovi_upload(title.strip(), description.strip(), uploaded_file, admin_id)
            st.success("File hasil analisis berhasil disimpan.")
            st.rerun()

st.subheader("Riwayat Upload")
uploads = get_jamovi_uploads()
st.dataframe(uploads, use_container_width=True, hide_index=True)

if not uploads.empty:
    selected_id = st.selectbox(
        "Pilih file",
        uploads["id"].tolist(),
        format_func=lambda value: uploads.loc[uploads["id"] == value, "file_name"].iloc[0],
    )
    file_data = get_jamovi_file(int(selected_id))
    if file_data:
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "Download File Analisis",
                bytes(file_data["file_content"]),
                file_name=file_data["file_name"],
                mime=file_data["file_type"],
            )
        with col2:
            if st.button("Hapus File", type="secondary"):
                delete_jamovi_upload(int(selected_id))
                st.success("File berhasil dihapus.")
                st.rerun()
