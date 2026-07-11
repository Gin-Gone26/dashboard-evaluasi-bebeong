# Mockup Perancangan Antarmuka

Mockup berikut menggambarkan rancangan antarmuka sistem dashboard evaluasi penerimaan ASN terhadap Aplikasi BEBEONG Banjar Super Apps. Rancangan dibuat sederhana dan formal agar sesuai sebagai media pengumpulan data penelitian serta dashboard pengelolaan data oleh admin.

## Mockup Halaman Responden

```text
+--------------------------------------------------------------------------+
|                         PENELITIAN SKRIPSI                               |
|        Kuesioner Evaluasi Aplikasi BEBEONG Banjar Super Apps              |
|  Penelitian mandiri mengenai penerimaan pengguna terhadap aplikasi        |
|  BEBEONG Banjar Super Apps menggunakan Technology Acceptance Model (TAM).  |
+--------------------------------------------------------------------------+

+--------------------+--------------------+--------------------+-----------+
| Peneliti           | NIM                | Program Studi      | Tahun     |
| Ahmad Akbar G.     | 22110246           | Teknik Informatika | 2026      |
+--------------------+--------------------+--------------------+-----------+

+--------------------------------------------------------------------------+
| Petunjuk Pengisian                                                       |
| Isi data umum responden tanpa identitas pribadi. Pilih satu jawaban       |
| pada setiap pernyataan dengan skala 1 sampai 5.                           |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| Data Umum Responden                                                      |
| +-------------------------------+ +------------------------------------+ |
| | Jenis Kelamin                 | | Unit Kerja                         | |
| +-------------------------------+ +------------------------------------+ |
| | Usia                          | | Jabatan                            | |
| +-------------------------------+ +------------------------------------+ |
| | Pendidikan Terakhir           | | Masa Kerja                         | |
| +-------------------------------+ +------------------------------------+ |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| Kuesioner TAM                                                            |
| PU - Perceived Usefulness                                                |
| PU1. Pernyataan kuesioner                                                |
| ( ) 1 Sangat Tidak Setuju  ( ) 2  ( ) 3  ( ) 4  ( ) 5 Sangat Setuju      |
|                                                                          |
| PEOU - Perceived Ease of Use                                             |
| PEOU1. Pernyataan kuesioner                                              |
| ( ) 1 Sangat Tidak Setuju  ( ) 2  ( ) 3  ( ) 4  ( ) 5 Sangat Setuju      |
|                                                                          |
| BI - Behavioral Intention                                                |
| BI1. Pernyataan kuesioner                                                |
| ( ) 1 Sangat Tidak Setuju  ( ) 2  ( ) 3  ( ) 4  ( ) 5 Sangat Setuju      |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| [ ] Saya bersedia menjadi responden penelitian ini.                       |
|                                                                          |
|                         [ Kirim Kuesioner ]                              |
+--------------------------------------------------------------------------+
```

## Mockup Dashboard Admin

```text
+--------------------------------------------------------------------------+
| Panel Admin                                                              |
| Dashboard Admin                                                          |
| Ringkasan visual hasil pengumpulan data evaluasi penerimaan ASN.          |
+--------------------------------------------------------------------------+

+-------------+-------------+-------------+-------------+-------------+
| Responden   | Jawaban     | Rata PEOU   | Rata PU     | Rata BI     |
|     120     |     120     |    4.12     |    4.20     |    4.05     |
+-------------+-------------+-------------+-------------+-------------+

+--------------------------------------------------------------------------+
| Grafik Rata-rata Variabel TAM                                            |
| PEOU  ██████████                                                         |
| PU    ███████████                                                        |
| BI    █████████                                                          |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| Grafik Distribusi Jawaban Likert                                         |
| PU1 | 1 | 2 | 3 | 4 | 5                                                  |
| PU2 | 1 | 2 | 3 | 4 | 5                                                  |
+--------------------------------------------------------------------------+
```

## Mockup Halaman Data Responden

```text
+--------------------------------------------------------------------------+
| Panel Admin                                                              |
| Data Responden                                                           |
| Kelola data umum responden yang telah mengisi kuesioner TAM.              |
+--------------------------------------------------------------------------+

+----------------+----------------+----------------+----------------+
| Jenis Kelamin  | Unit Kerja     | Dari Tanggal   | Sampai Tanggal |
+----------------+----------------+----------------+----------------+

+-------------------------------+ +-------------------------------+
| [ Download CSV Responden ]    | | [ Download Excel Responden ]  |
+-------------------------------+ +-------------------------------+

+--------------------------------------------------------------------------+
| Tabel Data Responden                                                     |
| id | gender | age | work_unit | position_name | education | masa_kerja   |
+--------------------------------------------------------------------------+
```

## Mockup Halaman Hasil Kuesioner

```text
+--------------------------------------------------------------------------+
| Panel Admin                                                              |
| Hasil Kuesioner TAM                                                      |
| Lihat jawaban skala Likert PU, PEOU, dan BI.                              |
+--------------------------------------------------------------------------+

+----------------+----------------+----------------+----------------+
| Jenis Kelamin  | Unit Kerja     | Dari Tanggal   | Sampai Tanggal |
+----------------+----------------+----------------+----------------+

+-------------------------------+ +-------------------------------+
| [ Download CSV untuk Jamovi ] | | [ Download Excel untuk Jamovi ]|
+-------------------------------+ +-------------------------------+

+--------------------------------------------------------------------------+
| Tabel Hasil Kuesioner                                                    |
| questionnaire_id | respondent_id | PU1 | PU2 | ... | PEOU1 | ... | BI6    |
+--------------------------------------------------------------------------+
```

## Mockup Halaman Upload Jamovi

```text
+--------------------------------------------------------------------------+
| Panel Admin                                                              |
| Upload Hasil Analisis Jamovi                                             |
| Simpan arsip hasil analisis Jamovi seperti OMV, CSV, Excel, PDF, HTML.    |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| Judul Hasil Analisis  [ .............................................. ]  |
| Catatan               [ .............................................. ]  |
| Pilih File            [ Choose File ]                                    |
|                                                                          |
|                         [ Simpan Upload ]                                |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| Riwayat Upload                                                           |
| id | title | file_name | file_type | uploaded_by | uploaded_at           |
+--------------------------------------------------------------------------+
```

## Mockup Halaman Laporan Evaluasi

```text
+--------------------------------------------------------------------------+
| Panel Admin                                                              |
| Laporan Evaluasi                                                         |
| Ringkasan laporan evaluasi penerimaan ASN terhadap aplikasi BEBEONG.      |
+--------------------------------------------------------------------------+

+-------------------------------+ +-------------------------------+
| Total Responden               | | Total Jawaban Kuesioner       |
+-------------------------------+ +-------------------------------+

+--------------------------------------------------------------------------+
| Rata-rata Variabel TAM                                                   |
| Variabel | Rata-rata                                                     |
| PEOU     | 4.12                                                          |
| PU       | 4.20                                                          |
| BI       | 4.05                                                          |
+--------------------------------------------------------------------------+

                             [ Download Laporan HTML ]
```
