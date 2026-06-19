# Use Case

```mermaid
flowchart LR
    ASN["ASN"]
    Admin["Admin"]
    Sistem["Dashboard Evaluasi TAM"]

    ASN --> UC1["Mengisi data umum responden"]
    ASN --> UC2["Mengisi kuesioner TAM"]
    ASN --> UC3["Mengirim jawaban"]

    Admin --> UC4["Login"]
    Admin --> UC5["Melihat dashboard visualisasi"]
    Admin --> UC6["Mengelola data responden"]
    Admin --> UC7["Melihat hasil kuesioner"]
    Admin --> UC8["Filter data"]
    Admin --> UC9["Export Excel/CSV"]
    Admin --> UC10["Upload hasil analisis Jamovi"]
    Admin --> UC11["Unduh laporan evaluasi"]

    UC1 --> Sistem
    UC2 --> Sistem
    UC3 --> Sistem
    UC4 --> Sistem
    UC5 --> Sistem
    UC6 --> Sistem
    UC7 --> Sistem
    UC8 --> Sistem
    UC9 --> Sistem
    UC10 --> Sistem
    UC11 --> Sistem
```

## Skenario Utama ASN

1. ASN membuka aplikasi.
2. ASN mengisi data umum tanpa nama, NIP, email, atau identitas pribadi.
3. ASN mengisi 20 item kuesioner TAM.
4. ASN menekan tombol kirim.
5. Sistem menyimpan data umum responden dan jawaban ke MySQL.

## Skenario Utama Admin

1. Admin login.
2. Admin membuka dashboard.
3. Admin memantau jumlah responden dan grafik hasil.
4. Admin memfilter dan mengecek data.
5. Admin mengekspor data untuk dianalisis di Jamovi.
6. Admin mengunggah hasil analisis Jamovi.
7. Admin mengunduh laporan evaluasi.
