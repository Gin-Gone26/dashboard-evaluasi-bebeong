# Struktur Menu

Struktur menu sistem dibagi berdasarkan dua aktor utama, yaitu ASN sebagai responden dan admin sebagai pengelola data. ASN hanya mengakses halaman pengisian kuesioner, sedangkan admin memiliki akses ke halaman dashboard, data responden, hasil kuesioner, upload hasil analisis Jamovi, dan laporan evaluasi.

```mermaid
flowchart TD
    A["Dashboard Evaluasi TAM"] --> B["Halaman Responden"]
    A --> C["Login Admin"]

    B --> B1["Informasi Penelitian"]
    B --> B2["Data Umum Responden"]
    B --> B3["Kuesioner TAM"]
    B --> B4["Persetujuan Responden"]
    B --> B5["Kirim Kuesioner"]

    C --> D["Dashboard Admin"]
    D --> D1["Statistik Responden"]
    D --> D2["Grafik Rata-rata Variabel TAM"]
    D --> D3["Grafik Distribusi Jawaban"]

    D --> E["Data Responden"]
    E --> E1["Filter Data"]
    E --> E2["Tabel Data Responden"]
    E --> E3["Edit Data Responden"]
    E --> E4["Hapus Data Responden"]
    E --> E5["Export CSV/Excel"]

    D --> F["Hasil Kuesioner"]
    F --> F1["Filter Data"]
    F --> F2["Tabel Hasil Kuesioner"]
    F --> F3["Export CSV/Excel untuk Jamovi"]

    D --> G["Upload Jamovi"]
    G --> G1["Upload File Analisis"]
    G --> G2["Riwayat Upload"]
    G --> G3["Download/Hapus File"]

    D --> H["Laporan Evaluasi"]
    H --> H1["Ringkasan Data"]
    H --> H2["Rata-rata Variabel TAM"]
    H --> H3["Narasi Laporan"]
    H --> H4["Download Laporan HTML"]
```

Halaman responden berisi informasi penelitian, form data umum responden tanpa identitas pribadi, form kuesioner TAM, persetujuan responden, dan tombol kirim kuesioner. Halaman admin digunakan untuk mengelola data hasil pengisian kuesioner, menampilkan visualisasi, mengekspor data untuk Jamovi, mengarsipkan file hasil analisis, dan mengunduh laporan evaluasi.
