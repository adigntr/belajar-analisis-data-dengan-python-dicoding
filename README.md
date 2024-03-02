# Brazilian E-Commerce Public Dataset Analysis

## Overview
Proyek ini bertujuan untuk menganalisis dataset e-commerce publik dari Brazil menggunakan Streamlit untuk visualisasi dan interaktivitas, serta Pandas untuk manipulasi data. Analisis mencakup performa penjualan berdasarkan kota, penjualan bulanan, dan metode pembayaran yang digunakan.

## Features
- **Filtering by Date Range**: Pengguna dapat menentukan rentang waktu untuk analisis data.
- **Top 5 Sales by City**: Menampilkan 5 kota dengan penjualan tertinggi.
- **Monthly Sales Trend**: Menampilkan tren penjualan bulanan.
- **Payment Methods Breakdown**: Analisis distribusi nilai pembayaran berdasarkan metode pembayaran.

## How to Use
1. **Install Requirements**: Pastikan semua dependensi telah terpasang. Lihat bagian Installation untuk detailnya.
2. **Run the Streamlit App**: Jalankan aplikasi Streamlit menggunakan perintah `streamlit run your_script.py`.
3. **Interact with the Dashboard**: Gunakan sidebar untuk memilih rentang waktu dan lihat analisis data yang disajikan dalam dashboard.

## Installation
Pastikan Python telah terinstal pada sistem Anda. Instalasi dapat dilakukan dengan menjalankan perintah berikut di terminal atau command prompt:
```python
pip install -r requirements.txt
```
Setelah semua dependensi terinstal, jalankan aplikasi dengan:
```python
streamlit run dashboard.py
```

## Data Source
Data diperoleh dari [Brazilian E-Commerce Public Dataset](https://raw.githubusercontent.com/adigntr/dicoding-dataset/main/E-Commerce%20Public%20Dataset/main_df.csv), yang merupakan dataset publik mengenai transaksi e-commerce di Brazil.
