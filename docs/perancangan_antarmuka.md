# Perancangan Antarmuka

Perancangan antarmuka dilakukan untuk menghasilkan tampilan sistem yang sederhana, formal, responsif, dan mudah digunakan oleh responden maupun admin. Antarmuka dikembangkan menggunakan framework Streamlit dengan pendekatan dashboard web. Tampilan publik dibuat netral sebagai media penelitian pribadi, bukan sebagai aplikasi resmi instansi.

## Halaman Responden

Halaman responden merupakan halaman utama yang digunakan ASN untuk mengisi kuesioner. Pada bagian atas halaman terdapat judul penelitian, informasi peneliti, NIM, program studi, dan tahun penelitian. Setelah itu terdapat petunjuk pengisian, form data umum responden, daftar pertanyaan kuesioner TAM, pernyataan persetujuan responden, dan tombol kirim kuesioner.

Komponen utama halaman responden:

- Header penelitian.
- Informasi peneliti.
- Petunjuk pengisian.
- Form data umum responden.
- Form kuesioner TAM.
- Persetujuan responden.
- Tombol kirim kuesioner.
- Pesan berhasil atau pesan kesalahan.

## Halaman Login Admin

Login admin ditempatkan pada sidebar aplikasi. Admin memasukkan username dan password untuk mengakses halaman pengelolaan data. Jika login berhasil, sistem menampilkan tautan menuju Dashboard Admin. Jika login gagal, sistem menampilkan pesan kesalahan.

Komponen utama halaman login admin:

- Input username.
- Input password.
- Tombol login.
- Pesan status login.
- Tombol logout setelah berhasil login.

## Halaman Dashboard Admin

Halaman Dashboard Admin digunakan untuk menampilkan ringkasan hasil pengumpulan data. Informasi yang ditampilkan meliputi jumlah responden, jumlah jawaban, rata-rata variabel PEOU, PU, dan BI. Halaman ini juga menampilkan grafik rata-rata variabel TAM serta distribusi jawaban Likert.

Komponen utama halaman Dashboard Admin:

- Header halaman admin.
- Kartu statistik jumlah responden.
- Kartu statistik jumlah jawaban.
- Kartu rata-rata PEOU, PU, dan BI.
- Grafik rata-rata variabel TAM.
- Grafik distribusi jawaban Likert.

## Halaman Data Responden

Halaman Data Responden digunakan admin untuk mengelola data umum responden. Data yang ditampilkan bersifat anonim dan tidak memuat nama, NIP, atau email. Admin dapat melakukan filter data, melihat tabel data, mengunduh data dalam format CSV atau Excel, mengedit data umum responden, dan menghapus data jika diperlukan.

Komponen utama halaman Data Responden:

- Filter jenis kelamin.
- Filter unit kerja.
- Filter tanggal.
- Tombol export CSV.
- Tombol export Excel.
- Tabel data responden.
- Form edit data responden.
- Tombol hapus data responden.

## Halaman Hasil Kuesioner

Halaman Hasil Kuesioner digunakan untuk menampilkan jawaban kuesioner TAM yang telah dikirim oleh responden. Admin dapat memfilter data, melihat tabel hasil kuesioner, melihat ringkasan rata-rata variabel, dan mengekspor data ke format CSV atau Excel. File export tersebut digunakan sebagai bahan analisis lanjutan di Jamovi.

Komponen utama halaman Hasil Kuesioner:

- Filter data.
- Tombol export CSV untuk Jamovi.
- Tombol export Excel untuk Jamovi.
- Grafik rata-rata variabel TAM.
- Tabel hasil kuesioner.

## Halaman Upload Jamovi

Halaman Upload Jamovi digunakan untuk menyimpan file hasil analisis Jamovi. File yang diunggah berfungsi sebagai arsip dan tidak memengaruhi perhitungan grafik pada dashboard. Admin dapat mengunggah file, melihat riwayat upload, mengunduh ulang file, atau menghapus file.

Komponen utama halaman Upload Jamovi:

- Input judul hasil analisis.
- Input catatan.
- Upload file analisis.
- Tombol simpan upload.
- Tabel riwayat upload.
- Tombol download file.
- Tombol hapus file.

## Halaman Laporan Evaluasi

Halaman Laporan Evaluasi digunakan untuk menampilkan ringkasan hasil pengumpulan data dan visualisasi rata-rata variabel TAM. Halaman ini juga menyediakan narasi laporan dan tombol untuk mengunduh laporan evaluasi dalam format HTML.

Komponen utama halaman Laporan Evaluasi:

- Ringkasan total responden.
- Ringkasan total jawaban kuesioner.
- Tabel rata-rata variabel TAM.
- Grafik rata-rata variabel TAM.
- Narasi laporan evaluasi.
- Tombol download laporan HTML.
