DICODING DASHBOARD

# Streamlit Application

This is a Streamlit application that runs a Python file using Streamlit on macOS. Follow the instructions below to set up and run the application.

Proyek Analisis Penyewaan Sepeda

# Deskripsi Proyek

Proyek ini menganalisis data penyewaan sepeda di wilayah tertentu dengan memanfaatkan dua dataset utama: day.csv dan hour.csv. Proyek ini mencakup visualisasi data serta pengolahan dan analisis dengan Python.

# Dataset

Proyek ini menggunakan dua dataset yang berisi informasi penyewaan sepeda harian dan per jam:

day.csv: Dataset yang berisi informasi penyewaan sepeda harian.
hour.csv: Dataset yang berisi informasi penyewaan sepeda per jam.

- Penjelasan Kolom
instant: Indeks record.
dteday: Tanggal pencatatan.
season: Musim (1: musim semi, 2: musim panas, 3: musim gugur, 4: musim dingin).
yr: Tahun (0: 2011, 1: 2012).
mnth: Bulan (1 hingga 12).
holiday: Apakah hari tersebut hari libur (1: ya, 0: tidak).
weekday: Hari dalam minggu (0: Minggu hingga 6: Sabtu).
workingday: Apakah hari kerja (1: ya, 0: tidak).
weathersit: Kondisi cuaca (1: cerah, 2: berkabut, 3: hujan ringan, 4: hujan deras).
temp: Suhu normalisasi (nilai antara 0 hingga 1).
atemp: Suhu "terasa" normalisasi.
hum: Kelembapan normalisasi.
windspeed: Kecepatan angin normalisasi.
casual: Jumlah penyewaan oleh pengguna non-terdaftar.
registered: Jumlah penyewaan oleh pengguna terdaftar.
cnt: Total jumlah penyewaan sepeda.

# Struktur  
dicodingproject
>dashboard
>>dashboard.py
>>day_csv
>>hour_csv

>data
>>day_csv
>>hour_csv

>notebook.ipynb

>requirements.txt

>url.txt

# Setup Environment Terminal
pip install -r requirements.txt
python dashboard.py

# Run Streamlit App
streamlit run /Users/sakti/Downloads/dicodingproject/dashboard/dashboard.py

# You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://192.168.1.3:8501
