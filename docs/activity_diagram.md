# Activity Diagram

## Activity Diagram ASN

```mermaid
flowchart TD
    A([Mulai]) --> B[Mengakses dashboard kuesioner]
    B --> C[Membaca informasi penelitian]
    C --> D[Mengisi data umum responden]
    D --> E[Mengisi kuesioner TAM]
    E --> F[Mengisi saran atau masukan opsional]
    F --> G[Mencentang persetujuan responden]
    G --> H{Data lengkap?}

    H -- Tidak --> I[Menampilkan pesan kesalahan]
    I --> D

    H -- Ya --> J[Mengirim jawaban]
    J --> K[Menyimpan data umum responden]
    K --> L[Menyimpan hasil kuesioner TAM dan saran opsional]
    L --> M[Menampilkan pesan berhasil]
    M --> N([Selesai])
```

Activity diagram ASN menggambarkan alur responden dalam menggunakan dashboard kuesioner. Proses dimulai ketika ASN mengakses dashboard, membaca informasi penelitian, mengisi data umum tanpa mencantumkan identitas pribadi, mengisi kuesioner TAM, mengisi saran atau masukan secara opsional, memberikan persetujuan, dan mengirim jawaban. Sistem memvalidasi kelengkapan data. Jika data belum lengkap, sistem menampilkan pesan kesalahan. Jika data lengkap, sistem menyimpan data umum responden, hasil kuesioner, dan saran opsional ke database MySQL.

## Activity Diagram Admin

```mermaid
flowchart TD
    A([Mulai]) --> B[Mengakses dashboard]
    B --> C[Melakukan login admin]
    C --> D{Data login valid?}

    D -- Tidak --> E[Menampilkan pesan login gagal]
    E --> C

    D -- Ya --> F[Menampilkan dashboard admin]
    F --> G[Melihat statistik responden]
    G --> H[Melihat grafik hasil evaluasi]
    H --> I{Memilih menu pengelolaan}

    I --> J[Data Responden]
    J --> K[Melihat, memfilter, mengubah, atau menghapus data responden]
    K --> I

    I --> L[Hasil Kuesioner]
    L --> M[Melihat, memfilter, dan mengekspor data ke CSV atau Excel]
    M --> I

    I --> N[Upload Hasil Jamovi]
    N --> O[Mengunggah file hasil analisis Jamovi]
    O --> I

    I --> P[Laporan Evaluasi]
    P --> Q[Melihat ringkasan dan mengunduh laporan evaluasi]
    Q --> I

    I --> R[Logout]
    R --> S([Selesai])
```

Activity diagram Admin menggambarkan alur admin dalam mengelola data hasil evaluasi. Admin melakukan login terlebih dahulu. Jika login valid, sistem menampilkan dashboard admin. Admin dapat melihat statistik dan grafik, mengelola data responden, melihat hasil kuesioner, mengekspor data, mengunggah hasil analisis Jamovi, mengunduh laporan evaluasi, dan keluar dari sistem melalui fitur logout.
