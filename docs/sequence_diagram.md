# Sequence Diagram

## Sequence Diagram ASN

```mermaid
sequenceDiagram
    actor ASN
    participant Antarmuka as Antarmuka Dashboard
    participant Sistem as Sistem Aplikasi
    participant Database as Database MySQL

    ASN->>Antarmuka: Mengakses halaman kuesioner
    Antarmuka-->>ASN: Menampilkan informasi penelitian dan form kuesioner

    ASN->>Antarmuka: Mengisi data umum responden
    ASN->>Antarmuka: Mengisi jawaban kuesioner TAM
    ASN->>Antarmuka: Memberikan persetujuan responden
    ASN->>Antarmuka: Mengirim kuesioner

    Antarmuka->>Sistem: Mengirim data responden dan jawaban kuesioner
    Sistem->>Sistem: Melakukan validasi kelengkapan data

    alt Data belum lengkap
        Sistem-->>Antarmuka: Mengirim status validasi gagal
        Antarmuka-->>ASN: Menampilkan pesan kesalahan
    else Data lengkap
        Sistem->>Database: Menyimpan data umum responden
        Database-->>Sistem: Mengirim ID responden
        Sistem->>Database: Menyimpan jawaban kuesioner TAM
        Database-->>Sistem: Mengirim status penyimpanan berhasil
        Sistem-->>Antarmuka: Mengirim status pengiriman berhasil
        Antarmuka-->>ASN: Menampilkan pesan berhasil
    end
```

Sequence diagram ASN menggambarkan interaksi antara ASN, antarmuka dashboard, sistem aplikasi, dan database MySQL. Setelah ASN mengisi data dan mengirim kuesioner, sistem melakukan validasi. Jika data lengkap, sistem menyimpan data umum responden dan jawaban kuesioner ke database.

## Sequence Diagram Admin

```mermaid
sequenceDiagram
    actor Admin
    participant Antarmuka as Antarmuka Dashboard
    participant Sistem as Sistem Aplikasi
    participant Database as Database MySQL
    participant Berkas as Berkas Export/Jamovi

    Admin->>Antarmuka: Mengakses halaman login admin
    Antarmuka-->>Admin: Menampilkan form login

    Admin->>Antarmuka: Memasukkan username dan password
    Antarmuka->>Sistem: Mengirim data login
    Sistem->>Database: Memeriksa data akun admin
    Database-->>Sistem: Mengirim data akun admin

    alt Login tidak valid
        Sistem-->>Antarmuka: Mengirim status login gagal
        Antarmuka-->>Admin: Menampilkan pesan login gagal
    else Login valid
        Sistem-->>Antarmuka: Mengirim status login berhasil
        Antarmuka-->>Admin: Menampilkan halaman dashboard admin

        Admin->>Antarmuka: Memilih menu dashboard admin
        Antarmuka->>Sistem: Meminta data ringkasan evaluasi
        Sistem->>Database: Mengambil data responden dan kuesioner
        Database-->>Sistem: Mengirim data evaluasi
        Sistem-->>Antarmuka: Mengirim data statistik dan visualisasi
        Antarmuka-->>Admin: Menampilkan statistik dan grafik evaluasi

        Admin->>Antarmuka: Memilih menu data responden atau hasil kuesioner
        Antarmuka->>Sistem: Mengirim permintaan data berdasarkan filter
        Sistem->>Database: Mengambil data sesuai filter
        Database-->>Sistem: Mengirim data hasil pencarian
        Sistem-->>Antarmuka: Mengirim data tabel
        Antarmuka-->>Admin: Menampilkan tabel data

        opt Mengelola data responden
            Admin->>Antarmuka: Mengubah atau menghapus data responden
            Antarmuka->>Sistem: Mengirim permintaan perubahan data
            Sistem->>Database: Memperbarui atau menghapus data
            Database-->>Sistem: Mengirim status proses berhasil
            Sistem-->>Antarmuka: Mengirim status perubahan data
            Antarmuka-->>Admin: Menampilkan notifikasi berhasil
        end

        opt Mengekspor data
            Admin->>Antarmuka: Memilih export CSV atau Excel
            Antarmuka->>Sistem: Meminta pembuatan berkas export
            Sistem->>Berkas: Membuat berkas CSV atau Excel
            Berkas-->>Sistem: Menghasilkan berkas export
            Sistem-->>Antarmuka: Mengirim berkas export
            Antarmuka-->>Admin: Mengunduh berkas export
        end

        opt Mengunggah hasil analisis Jamovi
            Admin->>Antarmuka: Mengunggah berkas hasil analisis Jamovi
            Antarmuka->>Sistem: Mengirim berkas hasil analisis
            Sistem->>Database: Menyimpan berkas hasil analisis
            Database-->>Sistem: Mengirim status penyimpanan berhasil
            Sistem-->>Antarmuka: Mengirim status upload berhasil
            Antarmuka-->>Admin: Menampilkan pesan upload berhasil
        end

        opt Mengunduh laporan evaluasi
            Admin->>Antarmuka: Memilih menu laporan evaluasi
            Antarmuka->>Sistem: Meminta ringkasan laporan
            Sistem->>Database: Mengambil data laporan
            Database-->>Sistem: Mengirim data laporan
            Sistem->>Berkas: Membuat laporan evaluasi
            Berkas-->>Sistem: Menghasilkan berkas laporan
            Sistem-->>Antarmuka: Mengirim laporan evaluasi
            Antarmuka-->>Admin: Mengunduh laporan evaluasi
        end
    end
```

Sequence diagram Admin menggambarkan interaksi antara admin, antarmuka dashboard, sistem aplikasi, database MySQL, dan berkas export atau hasil analisis. Admin dapat melakukan login, melihat visualisasi, mengelola data responden, mengekspor data, mengunggah file hasil analisis Jamovi, dan mengunduh laporan evaluasi.
