import sqlite3
import pandas as pd

# CSV dosyasını oku
df = pd.read_csv("daily_data.csv")

# OLTP veritabanı oluştur
conn = sqlite3.connect("oltp.db")
cursor = conn.cursor()

# Eski tabloyu sil
cursor.execute("DROP TABLE IF EXISTS daily_weather")

# Tabloyu oluştur (gerekli tüm sütunlar)
cursor.execute("""
CREATE TABLE daily_weather (
    city_name TEXT,
    datetime TEXT,
    weather_code REAL,
    temperature_2m_max REAL,
    temperature_2m_min REAL,
    temperature_2m_mean REAL,
    apparent_temperature_max REAL,
    apparent_temperature_min REAL,
    apparent_temperature_mean REAL,
    sunrise TEXT,
    sunset TEXT,
    daylight_duration REAL,
    sunshine_duration REAL,
    precipitation_sum REAL,
    rain_sum REAL,
    snowfall_sum REAL,
    precipitation_hours REAL,
    wind_speed_10m_max REAL,
    wind_gusts_10m_max REAL,
    wind_direction_10m_dominant TEXT,
    shortwave_radiation_sum REAL,
    et0_fao_evapotranspiration REAL
)
""")

# Verileri veritabanına kaydet
df.to_sql("daily_weather", conn, if_exists="append", index=False)

print("✔ Veri başarıyla OLTP veritabanına aktarıldı.\n")

# 1) Bangkok verileri
print("1) Bangkok verilerini getir:")
cursor.execute("""
    SELECT city_name, datetime, temperature_2m_max
    FROM daily_weather
    WHERE city_name LIKE '%Bangkok%'
    LIMIT 10
""")
print(cursor.fetchall(), "\n")

# 2) 35°C üzeri sıcaklıklar
print("2) Sıcaklığı 35°C’ten yüksek olan günler:")
cursor.execute("""
    SELECT city_name, datetime, temperature_2m_max
    FROM daily_weather
    WHERE temperature_2m_max > 35
    LIMIT 20
""")
print(cursor.fetchall(), "\n")

conn.close()
