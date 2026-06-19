# Desain Database MySQL

## Tabel `admins`

Menyimpan akun administrator.

| Kolom | Tipe | Keterangan |
|---|---|---|
| id | INT PK | ID admin |
| username | VARCHAR(50) UNIQUE | Username login |
| password_hash | VARCHAR(255) | Hash password |
| full_name | VARCHAR(100) | Nama admin |
| created_at | TIMESTAMP | Waktu dibuat |

## Tabel `respondents`

Menyimpan data umum responden tanpa nama, NIP, email, atau identitas pribadi.

| Kolom | Tipe | Keterangan |
|---|---|---|
| id | INT PK | ID responden |
| gender | ENUM | Jenis kelamin |
| age | INT | Usia |
| work_unit | VARCHAR(150) | Unit kerja |
| position_name | VARCHAR(120) | Jabatan |
| education | VARCHAR(50) | Pendidikan terakhir |
| years_of_service | INT | Masa kerja |
| created_at | TIMESTAMP | Waktu input |
| updated_at | TIMESTAMP | Waktu update |

## Tabel `questionnaires`

Menyimpan jawaban kuesioner TAM skala Likert 1-5.

| Kolom | Tipe | Keterangan |
|---|---|---|
| id | INT PK | ID jawaban |
| respondent_id | INT FK | Relasi ke responden |
| PEOU1-PEOU7 | TINYINT | Jawaban variabel PEOU |
| PU1-PU7 | TINYINT | Jawaban variabel PU |
| BI1-BI6 | TINYINT | Jawaban variabel BI |
| submitted_at | TIMESTAMP | Waktu submit |

## Tabel `jamovi_uploads`

Menyimpan file hasil analisis Jamovi.

| Kolom | Tipe | Keterangan |
|---|---|---|
| id | INT PK | ID upload |
| title | VARCHAR(150) | Judul file |
| description | TEXT | Catatan admin |
| file_name | VARCHAR(255) | Nama file |
| file_type | VARCHAR(100) | MIME type |
| file_content | LONGBLOB | Isi file |
| uploaded_by | INT FK | Admin pengunggah |
| uploaded_at | TIMESTAMP | Waktu upload |

