from datetime import date

import pandas as pd
import plotly.express as px
import streamlit as st

from src.constants import QUESTION_COLUMNS


def apply_responsive_styles(hide_page_navigation: bool = False) -> None:
    navigation_style = (
        '[data-testid="stSidebarNav"] { display: none; }'
        if hide_page_navigation
        else ""
    )
    st.markdown(
        """
        <style>
        :root {
            --civic-navy: #123b5d;
            --civic-blue: #176b87;
            --service-green: #2e7d5b;
            --civic-gold: #c79a3b;
            --surface: #f4f7f9;
            --border: #dce4e9;
            --text: #17212b;
        }

        __NAVIGATION_STYLE__

        .stApp {
            background: var(--surface);
        }

        .block-container {
            max-width: 1120px;
            padding-top: 1.25rem;
            padding-bottom: 2.5rem;
        }

        h1 {
            color: var(--civic-navy);
            font-size: 2rem;
            line-height: 1.2;
        }

        h2, h3 {
            color: var(--civic-navy);
            line-height: 1.25;
        }

        .institution-header {
            display: grid;
            grid-template-columns: 76px minmax(0, 1fr) 76px;
            gap: 1.25rem;
            align-items: center;
            background: #ffffff;
            border-top: 5px solid var(--civic-navy);
            border-bottom: 1px solid var(--border);
            padding: 1.15rem 1.35rem;
            margin-bottom: 1rem;
        }

        .logo-placeholder {
            width: 68px;
            height: 68px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px solid var(--civic-gold);
            border-radius: 50%;
            background: var(--civic-navy);
            color: #ffffff;
            font-size: 0.78rem;
            font-weight: 700;
            text-align: center;
            line-height: 1.1;
        }

        .institution-copy {
            text-align: center;
        }

        .institution-name {
            color: var(--civic-navy);
            font-size: 0.86rem;
            font-weight: 700;
            letter-spacing: 0;
            margin-bottom: 0.25rem;
            text-transform: uppercase;
        }

        .public-title {
            color: var(--text);
            font-size: 1.65rem;
            font-weight: 750;
            line-height: 1.25;
            margin: 0;
        }

        .public-subtitle {
            color: #556572;
            font-size: 0.92rem;
            line-height: 1.5;
            margin: 0.45rem auto 0;
            max-width: 760px;
        }

        .research-meta {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 1px;
            overflow: hidden;
            margin: 0 0 1.25rem;
            background: var(--border);
            border: 1px solid var(--border);
        }

        .research-meta-item {
            min-width: 0;
            background: #ffffff;
            padding: 0.8rem 0.9rem;
        }

        .research-meta-label {
            color: #6b7780;
            font-size: 0.72rem;
            font-weight: 650;
            text-transform: uppercase;
        }

        .research-meta-value {
            color: var(--text);
            font-size: 0.88rem;
            font-weight: 600;
            line-height: 1.35;
            margin-top: 0.25rem;
            overflow-wrap: anywhere;
        }

        .survey-intro {
            background: #ffffff;
            border-left: 4px solid var(--service-green);
            padding: 1rem 1.1rem;
            margin-bottom: 1rem;
        }

        .survey-intro strong {
            color: var(--civic-navy);
        }

        .privacy-note {
            background: #eef5f1;
            border: 1px solid #cfe1d7;
            color: #244b39;
            padding: 0.9rem 1rem;
            margin: 0.75rem 0 1rem;
            line-height: 1.55;
        }

        .public-footer {
            border-top: 1px solid var(--border);
            color: #64727d;
            font-size: 0.78rem;
            line-height: 1.5;
            margin-top: 1.5rem;
            padding-top: 1rem;
            text-align: center;
        }

        .admin-page-header {
            background: #ffffff;
            border-left: 5px solid var(--civic-navy);
            border-top: 1px solid var(--border);
            border-right: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            border-radius: 8px;
            margin-bottom: 1rem;
            padding: 1rem 1.1rem;
        }

        .admin-page-kicker {
            color: var(--service-green);
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0;
            margin-bottom: 0.25rem;
            text-transform: uppercase;
        }

        .admin-page-title {
            color: var(--civic-navy);
            font-size: 1.65rem;
            font-weight: 750;
            line-height: 1.25;
            margin: 0;
        }

        .admin-page-description {
            color: #5d6974;
            font-size: 0.92rem;
            line-height: 1.5;
            margin: 0.45rem 0 0;
            max-width: 820px;
        }

        .admin-section-note {
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: 8px;
            color: #52616d;
            line-height: 1.55;
            margin-bottom: 1rem;
            padding: 0.9rem 1rem;
        }

        .admin-danger-note {
            background: #fff7ed;
            border: 1px solid #fed7aa;
            border-radius: 8px;
            color: #8a4b14;
            line-height: 1.55;
            margin: 0.75rem 0 1rem;
            padding: 0.9rem 1rem;
        }

        div[data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 0.85rem 1rem;
        }

        div[data-testid="stForm"] {
            background: #ffffff;
            border: 1px solid var(--border);
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

        .stFormSubmitButton button[kind="primary"] {
            background: var(--civic-navy);
            border-color: var(--civic-navy);
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid var(--border);
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

            .institution-header {
                grid-template-columns: 52px minmax(0, 1fr) 52px;
                gap: 0.65rem;
                padding: 0.85rem 0.7rem;
            }

            .logo-placeholder {
                width: 48px;
                height: 48px;
                font-size: 0.58rem;
            }

            .institution-name {
                font-size: 0.68rem;
            }

            .public-title {
                font-size: 1.15rem;
            }

            .public-subtitle {
                font-size: 0.78rem;
                line-height: 1.4;
            }

            .admin-page-title {
                font-size: 1.28rem;
            }

            .research-meta {
                grid-template-columns: 1fr 1fr;
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
        """.replace("__NAVIGATION_STYLE__", navigation_style),
        unsafe_allow_html=True,
    )


def render_public_header() -> None:
    st.markdown(
        """
        <header class="institution-header">
            <div class="logo-placeholder">KOTA<br>BANJAR</div>
            <div class="institution-copy">
                <div class="institution-name">Diskominfo Kota Banjar</div>
                <h1 class="public-title">Dashboard Evaluasi Layanan Website BEBEONG</h1>
                <p class="public-subtitle">
                    Evaluasi penerimaan ASN menggunakan Technology Acceptance Model (TAM)
                    pada variabel PU, PEOU, dan BI.
                </p>
            </div>
            <div class="logo-placeholder">DIS<br>KOMINFO</div>
        </header>
        <section class="research-meta">
            <div class="research-meta-item">
                <div class="research-meta-label">Peneliti</div>
                <div class="research-meta-value">Ahmad Akbar Ginanjar</div>
            </div>
            <div class="research-meta-item">
                <div class="research-meta-label">NIM</div>
                <div class="research-meta-value">22110246</div>
            </div>
            <div class="research-meta-item">
                <div class="research-meta-label">Program Studi</div>
                <div class="research-meta-value">Teknik Informatika - Konsentrasi Sistem Informasi</div>
            </div>
            <div class="research-meta-item">
                <div class="research-meta-label">Tahun Penelitian</div>
                <div class="research-meta-value">2026</div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_public_footer() -> None:
    st.markdown(
        """
        <footer class="public-footer">
            Penelitian oleh Ahmad Akbar Ginanjar (22110246) ·
            Teknik Informatika, Konsentrasi Sistem Informasi · 2026
        </footer>
        """,
        unsafe_allow_html=True,
    )


def render_admin_page_header(title: str, description: str, kicker: str = "Panel Admin") -> None:
    st.markdown(
        f"""
        <section class="admin-page-header">
            <div class="admin-page-kicker">{kicker}</div>
            <h1 class="admin-page-title">{title}</h1>
            <p class="admin-page-description">{description}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_admin_note(text: str, danger: bool = False) -> None:
    css_class = "admin-danger-note" if danger else "admin-section-note"
    st.markdown(f'<div class="{css_class}">{text}</div>', unsafe_allow_html=True)


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

