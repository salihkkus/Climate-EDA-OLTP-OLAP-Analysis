import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV dosyasını oku
df = pd.read_csv(r"C:\Users\Salih\Desktop\OLAP+OLTP+EDA\daily_data.csv")

# ----------------------------------------------------------
# 1) ŞEHİRLERİN ORTALAMA SICAKLIK KARŞILAŞTIRMASI (BARPLOT)
# ----------------------------------------------------------
plt.figure(figsize=(14,8))
city_temp = df.groupby("city_name")["temperature_2m_mean"].mean().sort_values(ascending=False).head(20)
city_temp.plot(kind="bar")
plt.title("En Yüksek Ortalama Sıcaklığa Sahip 20 Şehir")
plt.ylabel("Ortalama Sıcaklık (°C)")
plt.xticks(rotation=75)
plt.show()

# ----------------------------------------------------------
# 2) SICAKLIK vs YAĞIŞ İLİŞKİSİ (SCATTER)
# ----------------------------------------------------------
plt.figure(figsize=(10,6))
plt.scatter(df["temperature_2m_mean"], df["precipitation_sum"])
plt.title("Sıcaklık - Yağış İlişkisi")
plt.xlabel("Ortalama Sıcaklık (°C)")
plt.ylabel("Toplam Yağış (mm)")
plt.show()

# ----------------------------------------------------------
# 3) RÜZGAR HIZI DAĞILIMI
# ----------------------------------------------------------
plt.figure(figsize=(10,6))
df["wind_speed_10m_max"].plot(kind="hist", bins=50)
plt.title("Rüzgar Hızı Dağılımı")
plt.xlabel("Rüzgar Hızı (m/s)")
plt.show()

# ----------------------------------------------------------
# 4) GÜN UZUNLUĞU ZAMAN SERİSİ
# ----------------------------------------------------------
plt.figure(figsize=(14,7))
df_sorted = df.sort_values("datetime")
plt.plot(df_sorted["datetime"], df_sorted["daylight_duration"])
plt.title("Gün Uzunluğunun Zaman İçindeki Değişimi")
plt.xlabel("Tarih")
plt.ylabel("Gün Uzunluğu (saniye)")
plt.xticks(rotation=45)
plt.show()

# ----------------------------------------------------------
# 5) HAVA DURUMU KODLARINA GÖRE SICAKLIK DAĞILIMI (BOXPLOT)
# ----------------------------------------------------------
plt.figure(figsize=(12,6))
df.boxplot(column="temperature_2m_mean", by="weather_code")
plt.title("Hava Durumu Kodlarına Göre Sıcaklık Dağılımı")
plt.suptitle("")  # üst yazıyı kaldırır
plt.xlabel("Weather Code")
plt.ylabel("Ortalama Sıcaklık (°C)")
plt.show()

# ----------------------------------------------------------
# 6) KORELASYON ISI HARİTASI (DETAYLI)
# ----------------------------------------------------------
plt.figure(figsize=(14,10))
sns.heatmap(df.corr(numeric_only=True), annot=False, cmap="coolwarm")
plt.title("Korelasyon Isı Haritası (Detaylı)")
plt.show()

