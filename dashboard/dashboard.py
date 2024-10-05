import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from scipy import stats
import matplotlib.ticker as mtick
from babel.numbers import format_currency

# Set seaborn style
sns.set(style='darkgrid')

#Judul
st.title('                               Bike Sharing Data Analysis')
st.write("🔻Desak Putu Tia Rusilia Wati")
st.write("🔻from ML-06")


#data
day_df = pd.read_csv("./dashboard/day.csv")
hour_df = pd.read_csv("./dashboard/hour.csv")
st.write("Day Dataset")
st.dataframe(day_df.head())
st.write("Hour Dataset")
st.dataframe(hour_df.head())

#Clean
st.write("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️")
st.subheader("Data yang fokus dianalisis setelah dilakukan cleaning data")
drop_col = ['instant', 'season', 'mnth', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'session']
existing_cols_to_drop = [col for col in drop_col if col in day_df.columns]
day_df_cleaned = day_df.drop(columns=existing_cols_to_drop)
st.write("Data yang akan dianalisis")
st.dataframe(day_df_cleaned.head())

#Q1
st.write("")
st.write("")
st.subheader("Question 1: Perbedaan Penyewaan Sepeda pada workingday dan Non-workingday")
workingday_df = day_df[day_df['workingday'] == 1]['cnt']
non_workingday_df = day_df[day_df['workingday'] == 0]['cnt']
mean_workingday = workingday_df.mean()
mean_non_workingday = non_workingday_df.mean()

st.write(f"Rata-rata Penyewaan pada workingday: {mean_workingday:.2f}")
st.write(f"Rata-rata Penyewaan pada Hari Non-workingday: {mean_non_workingday:.2f}")

# Bar plot
categories = ['Workingday', 'Non-Workingday']
means = [mean_workingday, mean_non_workingday]

fig, ax = plt.subplots()
sns.barplot(x=categories, y=means, ax=ax)
ax.set_title("Perbandingan Rata-Rata Penyewaan Sepeda (Workingday vs Non-workingday)")
st.pyplot(fig)
st.write("Rata-rata penyewaan sepeda pada hari kerja (workingday) adalah 4584.82 penyewaan, sedangkan pada hari non-kerja (akhir pekan atau hari libur), rata-rata penyewaan adalah 4330.17.")
st.write("Perbedaan rata-rata penyewaan sepeda antara hari kerja dan hari non-kerja tidak terlalu signifikan, meskipun hari kerja menunjukkan sedikit peningkatan")
st.write("Mengindikasikan bahwa sepeda digunakan secara konsisten baik pada hari kerja maupun hari libur/akhir pekan.")

#Q2
st.write("")
st.write("")
st.subheader("Question 2: Tren Penyewaan Berdasarkan Jam dan Perbandingan Jam Pagi")
hourly_rentals = hour_df.groupby('hr')['cnt'].mean()
fig2, ax2 = plt.subplots()
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker='o', ax=ax2)
ax2.set_title("Tren Penyewaan Sepeda Berdasarkan Jam")
ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig2)
st.write("Puncak penggunaan sepeda terjadi pada jam 17:00 dengan rata-rata lebih dari 400 penyewaan di mana menunjukkan bahwa banyak pengguna yang menggunakan sepeda pada sore hari. Peningkatan besar kedua terjadi pada jam 08:00-09:00 dengan jumlah penyewaan mendekati 300-400 penyewaan per jam. ")

#clusterkan jam
earlymorning_df = hour_df[(hour_df['hr'] >= 0) & (hour_df['hr'] < 6)]
morning_df = hour_df[(hour_df['hr'] >= 6) & (hour_df['hr'] < 12)]
afternoon_df = hour_df[(hour_df['hr'] >= 12) & (hour_df['hr'] < 18)]
evening_df = hour_df[(hour_df['hr'] >= 18) & (hour_df['hr'] < 23)]
time_periods = ['Subuh (00:00-06:00)', 'Pagi (06:00-12:00)', 'Siang (12:00-18:00)', 'Sore (18:00-23:00)']
means_time = [earlymorning_df['cnt'].mean(), morning_df['cnt'].mean(), afternoon_df['cnt'].mean(), evening_df['cnt'].mean()]

fig3, ax3 = plt.subplots()
sns.barplot(x=time_periods, y=means_time, ax=ax3)
ax3.set_title("Perbandingan Rata-Rata Penyewaan Sepeda Berdasarkan Waktu")
ax3.set_xlabel("Periode Waktu")
ax3.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig3)
st.write("Jam pagi (06:00 - 12:00) memang menunjukkan penggunaan sepeda yang signifikan, dengan rata-rata penyewaan sekitar 200 sepeda per jam. Namun, tidak lebih unggul dibandingkan periode siang (12:00 - 18:00), yang mencatat rata-rata penyewaan lebih tinggi, mendekati 300 penyewaan per jam. Periode siang memiliki penggunaan sepeda tertinggi dibandingkan semua periode waktu lainnya")

#Q3
st.write("")
st.write("")
st.subheader("Question 3: Peningkatan Total Penyewaan antara 2011 dan 2012")
yearly_rentals = day_df.groupby('yr').agg({
    'cnt': ['sum']
}).reset_index()
yearly_rentals['yr'] = yearly_rentals['yr'].replace({0: '2011', 1: '2012'})

fig4, ax4 = plt.subplots()
sns.barplot(x=yearly_rentals['yr'], y=yearly_rentals['cnt']['sum'], ax=ax4)
ax4.set_title("Total Penyewaan Sepeda per Tahun (2011 vs 2012)")
ax4.set_xlabel("Tahun")
ax4.set_ylabel("Jumlah Total Penyewaan")
ax4.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x):,}'))
st.pyplot(fig4)
st.write("Pada tahun 2011, total penyewaan sepeda adalah sekitar 1,243,103 dan tahun 2012, total penyewaan sepeda meningkat secara signifikan menjadi sekitar 2,049,576. Peningkatan ini menunjukkan bahwa penggunaan layanan penyewaan sepeda menjadi jauh lebih populer pada tahun 2012 dibandingkan dengan 2011.")
st.write("Terjadi peningkatan yang sangat signifikan dalam total jumlah penyewaan sepeda dari tahun 2011 ke tahun 2012.")