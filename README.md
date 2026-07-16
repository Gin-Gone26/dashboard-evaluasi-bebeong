# Dashboard Evaluasi Penerimaan ASN terhadap Layanan E-Government pada Aplikasi BEBEONG Banjar Super Apps

Judul skripsi:

**Pengembangan Dashboard Evaluasi Penerimaan ASN terhadap Layanan E-Government pada Aplikasi BEBEONG Banjar Super Apps Menggunakan Technology Acceptance Model (TAM)**

## Ringkasan Sistem

Aplikasi ini dibuat dengan Python Streamlit dan MySQL. Dashboard berfungsi untuk:

- Pengisian data umum responden tanpa nama, NIP, email, atau identitas pribadi.
- Pengisian kuesioner TAM skala Likert 1-5.
- Pengisian saran atau masukan secara opsional.
- Penyimpanan data responden dan jawaban ke MySQL.
- Pengelolaan data oleh admin.
- Filter, visualisasi, dan export data Excel/CSV.
- Upload hasil analisis Jamovi.
- Penyusunan dan unduh laporan evaluasi.

Dashboard tidak menghitung validitas, reliabilitas, atau regresi TAM. Analisis statistik lanjutan dilakukan di Jamovi menggunakan file export.

Tampilan publik dibuat netral sebagai media penelitian pribadi, bukan sebagai aplikasi resmi instansi.

## Struktur Folder

```text
.
├── app.py
├── pages/
│   ├── 1_Dashboard_Admin.py
│   ├── 2_Data_Responden.py
│   ├── 3_Hasil_Kuesioner.py
│   ├── 4_Upload_Jamovi.py
│   └── 5_Laporan_Evaluasi.py
├── src/
│   ├── config.py
│   ├── constants.py
│   ├── db.py
│   ├── security.py
│   ├── repositories/
│   │   ├── admin_repository.py
│   │   ├── analysis_repository.py
│   │   └── survey_repository.py
│   ├── services/
│   │   └── export_service.py
│   └── utils/
│       ├── auth.py
│       └── ui.py
├── sql/
│   └── schema.sql
├── docs/
│   ├── analisis_kebutuhan.md
│   ├── activity_diagram.md
│   ├── desain_database.md
│   ├── erd.md
│   ├── mockup_antarmuka.md
│   ├── perancangan_antarmuka.md
│   ├── sequence_diagram.md
│   ├── streamlit_pages.md
│   ├── struktur_menu.md
│   └── use_case.md
├── uploads/
├── requirements.txt
└── .streamlit/secrets.example.toml
```

## Cara Menjalankan Lokal

1. Buat database MySQL:

```sql
CREATE DATABASE tam_bebeong CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Jalankan script di `sql/schema.sql`.

3. Salin `.streamlit/secrets.example.toml` menjadi `.streamlit/secrets.toml`, lalu sesuaikan koneksi MySQL.

4. Install dependensi:

```bash
pip install -r requirements.txt
```

5. Jalankan aplikasi:

```bash
streamlit run app.py
```

Saat pertama kali berjalan, aplikasi akan membuat akun admin dari konfigurasi:

- Username default: `admin`
- Password default: `admin123`

Ganti password tersebut sebelum digunakan untuk penelitian sebenarnya.

## Deploy Streamlit Cloud

Tambahkan secrets di menu Streamlit Cloud:

```toml
[mysql]
host = "HOST_MYSQL"
port = 3306
database = "tam_bebeong"
user = "USER_MYSQL"
password = "PASSWORD_MYSQL"
ssl_required = true

[admin]
username = "admin"
password = "password_kuat"
```

Pastikan server MySQL dapat diakses dari Streamlit Cloud.

