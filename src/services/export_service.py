from io import BytesIO

import pandas as pd


def dataframe_to_excel_bytes(dataframe: pd.DataFrame, sheet_name: str = "Data") -> bytes:
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        dataframe.to_excel(writer, sheet_name=sheet_name[:31], index=False)
    return output.getvalue()


def dataframe_to_csv_bytes(dataframe: pd.DataFrame) -> bytes:
    return dataframe.to_csv(index=False).encode("utf-8-sig")


def build_report_html(summary: dict, variable_scores: pd.DataFrame) -> bytes:
    score_rows = "".join(
        f"<tr><td>{row['Variabel']}</td><td>{row['Rata-rata']}</td></tr>"
        for _, row in variable_scores.iterrows()
    )
    html = f"""
    <!doctype html>
    <html lang="id">
    <head>
      <meta charset="utf-8">
      <title>Laporan Evaluasi TAM Website Bebeong</title>
      <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; color: #1f2937; }}
        h1 {{ font-size: 24px; }}
        h2 {{ font-size: 18px; margin-top: 28px; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 12px; }}
        td, th {{ border: 1px solid #d1d5db; padding: 8px; text-align: left; }}
        th {{ background: #f3f4f6; }}
      </style>
    </head>
    <body>
      <h1>Laporan Evaluasi Penerimaan ASN terhadap Website Bebeong Kota Banjar</h1>
      <p>Metode: Technology Acceptance Model (TAM)</p>
      <h2>Ringkasan Data</h2>
      <table>
        <tr><th>Indikator</th><th>Jumlah</th></tr>
        <tr><td>Total responden</td><td>{summary.get("total_respondents", 0)}</td></tr>
        <tr><td>Total jawaban kuesioner</td><td>{summary.get("total_questionnaires", 0)}</td></tr>
      </table>
      <h2>Rata-rata Variabel TAM</h2>
      <table>
        <tr><th>Variabel</th><th>Rata-rata</th></tr>
        {score_rows}
      </table>
      <h2>Catatan</h2>
      <p>Dashboard ini digunakan untuk pengumpulan, pengelolaan, export, dan visualisasi data.
      Analisis statistik lanjutan seperti validitas, reliabilitas, dan regresi dilakukan menggunakan Jamovi.</p>
    </body>
    </html>
    """
    return html.encode("utf-8")
