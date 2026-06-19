# Analisis Kebutuhan Sistem

## Latar Belakang

Aplikasi BEBEONG Banjar Super Apps merupakan layanan e-government yang perlu dievaluasi dari sisi penerimaan pengguna. Penelitian menggunakan Technology Acceptance Model (TAM) dengan tiga variabel utama:

- Perceived Ease of Use (PEOU)
- Perceived Usefulness (PU)
- Behavioral Intention (BI)

## Tujuan Sistem

Sistem bertujuan menjadi media pengumpulan, pengelolaan, export, dan visualisasi data kuesioner TAM. Perhitungan statistik penelitian seperti uji validitas, reliabilitas, dan regresi dilakukan di Jamovi, bukan di dashboard.

## Aktor

1. ASN
   - Mengisi data umum responden tanpa identitas pribadi.
   - Mengisi 20 pertanyaan kuesioner TAM.
   - Mengirim jawaban.

2. Admin
   - Login.
   - Melihat data responden.
   - Melihat hasil kuesioner.
   - Melakukan filter data.
   - Export data ke Excel dan CSV.
   - Mengunggah hasil analisis Jamovi.
   - Melihat dashboard visualisasi hasil evaluasi.
   - Mengunduh laporan evaluasi.

## Kebutuhan Fungsional

- Sistem menyediakan form data umum responden tanpa nama, NIP, email, atau identitas pribadi.
- Sistem menyediakan form kuesioner TAM skala Likert 1-5.
- Sistem menyimpan data ke database MySQL.
- Sistem menyediakan autentikasi admin.
- Sistem menyediakan tabel responden dan tabel jawaban kuesioner.
- Sistem menyediakan fitur edit dan hapus data responden.
- Sistem menyediakan filter berdasarkan tanggal, jenis kelamin, dan unit kerja.
- Sistem menyediakan export Excel dan CSV.
- Sistem menyediakan upload file hasil analisis Jamovi.
- Sistem menyediakan dashboard visualisasi jumlah responden, distribusi jawaban, dan rata-rata variabel TAM.
- Sistem menyediakan laporan evaluasi yang dapat diunduh.

## Kebutuhan Non-Fungsional

- Berbasis web dan mudah diakses.
- Dibangun dengan Python Streamlit.
- Menggunakan MySQL sebagai penyimpanan data.
- Siap deploy ke Streamlit Cloud.
- Konfigurasi koneksi database menggunakan secrets agar aman.
- Antarmuka sederhana agar mudah digunakan oleh ASN dan admin.

