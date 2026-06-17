from datetime import date

import pandas as pd
import plotly.express as px
import streamlit as st

from src.constants import QUESTION_COLUMNS


def apply_responsive_styles() -> None:
    st.markdown(
        """
        <style>
        .block-container {
            max-width: 1180px;
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        h1 {
            font-size: 2rem;
            line-height: 1.2;
        }

        h2, h3 {
            line-height: 1.25;
        }

        div[data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 0.85rem 1rem;
        }

        div[data-testid="stForm"] {
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 1.2rem;
        }

        div[data-testid="stRadio"] > div {
            gap: 0.5rem 1rem;
        }

        .stButton button,
        .stDownloadButton button,
        .stFormSubmitButton button {
            width: 100%;
            border-radius: 8px;
            min-height: 2.6rem;
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            overflow: hidden;
        }

        @media (max-width: 768px) {
            .block-container {
                padding: 1rem 0.8rem 1.5rem;
            }

            h1 {
                font-size: 1.45rem;
            }

            h2 {
                font-size: 1.25rem;
            }

            h3 {
                font-size: 1.1rem;
            }

            div[data-testid="stForm"] {
                padding: 0.85rem;
            }

            div[data-testid="column"] {
                width: 100% !important;
                flex: 1 1 100% !important;
                min-width: 100% !important;
            }

            div[data-testid="stHorizontalBlock"] {
                gap: 0.35rem;
            }

            div[data-testid="stRadio"] > div {
                align-items: stretch;
            }

            div[data-testid="stRadio"] label {
                width: 100%;
                min-height: 2.2rem;
                padding-top: 0.15rem;
                padding-bottom: 0.15rem;
            }

            .stTextInput input,
            .stNumberInput input,
            .stSelectbox div[data-baseweb="select"] {
                min-height: 2.7rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_database_error(message: str) -> None:
    st.error("Aplikasi belum terhubung ke database MySQL.")
    st.info(
        "Periksa konfigurasi `.streamlit/secrets.toml` atau secrets di Streamlit Cloud, "
        "lalu pastikan database MySQL aktif dan dapat diakses."
    )
    with st.expander("Detail koneksi"):
        st.code(message)


def render_filters(prefix: str = "") -> dict:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender = st.selectbox("Jenis kelamin", ["Semua", "Laki-laki", "Perempuan"], key=f"{prefix}_gender")
    with col2:
        work_unit = st.text_input("Unit kerja", key=f"{prefix}_unit")
    with col3:
        start_date = st.date_input("Dari tanggal", value=None, key=f"{prefix}_start")
    with col4:
        end_date = st.date_input("Sampai tanggal", value=None, key=f"{prefix}_end")

    return {
        "gender": gender,
        "work_unit": work_unit.strip(),
        "start_date": start_date.isoformat() if isinstance(start_date, date) else None,
        "end_date": end_date.isoformat() if isinstance(end_date, date) else None,
    }


def variable_score_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    if dataframe.empty:
        return pd.DataFrame({"Variabel": ["PEOU", "PU", "BI"], "Rata-rata": [0.0, 0.0, 0.0]})
    return pd.DataFrame(
        {
            "Variabel": ["PEOU", "PU", "BI"],
            "Rata-rata": [
                round(dataframe["peou_avg"].mean(), 2),
                round(dataframe["pu_avg"].mean(), 2),
                round(dataframe["bi_avg"].mean(), 2),
            ],
        }
    )


def render_variable_chart(scores: pd.DataFrame) -> None:
    fig = px.bar(
        scores,
        x="Variabel",
        y="Rata-rata",
        color="Variabel",
        range_y=[0, 5],
        text="Rata-rata",
        color_discrete_sequence=["#2563eb", "#16a34a", "#ea580c"],
    )
    fig.update_layout(showlegend=False, margin=dict(l=10, r=10, t=20, b=10))
    st.plotly_chart(fig, use_container_width=True)


def render_likert_distribution(dataframe: pd.DataFrame) -> None:
    if dataframe.empty:
        st.info("Belum ada data kuesioner untuk ditampilkan.")
        return
    likert_data = dataframe[QUESTION_COLUMNS].melt(var_name="Pertanyaan", value_name="Skor")
    distribution = likert_data.groupby(["Pertanyaan", "Skor"]).size().reset_index(name="Jumlah")
    fig = px.bar(
        distribution,
        x="Pertanyaan",
        y="Jumlah",
        color="Skor",
        barmode="group",
        color_continuous_scale="Blues",
    )
    fig.update_layout(margin=dict(l=10, r=10, t=20, b=10))
    st.plotly_chart(fig, use_container_width=True)
