import streamlit as st

from src.db import init_database
from src.repositories.survey_repository import get_questionnaires, get_respondents
from src.utils.auth import render_admin_sidebar, require_admin
from src.utils.ui import (
    apply_responsive_styles,
    render_database_error,
    render_likert_distribution,
    render_variable_chart,
    variable_score_dataframe,
)


st.set_page_config(page_title="Dashboard Admin", page_icon="📊", layout="wide")
apply_responsive_styles()

try:
    init_database()
except Exception as exc:
    render_database_error(str(exc))
    st.stop()

require_admin()
render_admin_sidebar()

st.title("Dashboard Admin")
st.caption("Visualisasi hasil evaluasi penerimaan ASN terhadap Website Bebeong Kota Banjar.")

respondents = get_respondents()
questionnaires = get_questionnaires()
scores = variable_score_dataframe(questionnaires)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Responden", len(respondents))
col2.metric("Jawaban", len(questionnaires))
col3.metric("Rata-rata PEOU", scores.loc[scores["Variabel"] == "PEOU", "Rata-rata"].iloc[0])
col4.metric("Rata-rata PU", scores.loc[scores["Variabel"] == "PU", "Rata-rata"].iloc[0])
col5.metric("Rata-rata BI", scores.loc[scores["Variabel"] == "BI", "Rata-rata"].iloc[0])

st.subheader("Rata-rata Variabel TAM")
render_variable_chart(scores)

st.subheader("Distribusi Jawaban Likert")
render_likert_distribution(questionnaires)
