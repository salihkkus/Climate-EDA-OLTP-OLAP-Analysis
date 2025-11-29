import sqlite3
import pandas as pd

# OLTP veritabanına bağlan
conn = sqlite3.connect("oltp.db")

print("\n--- OLAP ANALİZLERİ ---\n")

# 1) Şehirlere göre en yüksek ortalama sıcaklığa sahip 10 şehir
df_avg_temp = pd.read_sql_query("""
    SELECT city_name, AVG(temperature_2m_max) AS avg_temp
    FROM daily_weather
    GROUP BY city_name
    ORDER BY avg_temp DESC
    LIMIT 10
""", conn)
print("1) Şehirlere göre en yüksek ortalama sıcaklığa sahip 10 şehir:")
print(df_avg_temp, "\n")

# 2) Şehirlere göre toplam yağış miktarına göre ilk 10 şehir
df_rain = pd.read_sql_query("""
    SELECT city_name, SUM(precipitation_sum) AS total_rain
    FROM daily_weather
    GROUP BY city_name
    ORDER BY total_rain DESC
    LIMIT 10
""", conn)
print("2) Şehirlere göre en çok toplam yağış alan 10 şehir:")
print(df_rain, "\n")

# 3) Şehirlere göre toplam güneşlenme süresi
df_sun = pd.read_sql_query("""
    SELECT city_name, SUM(sunshine_duration) AS total_sun
    FROM daily_weather
    GROUP BY city_name
    ORDER BY total_sun DESC
    LIMIT 10
""", conn)
print("3) Şehirlere göre toplam güneşlenme süresi (en yüksek 10 şehir):")
print(df_sun, "\n")

# 4) En yüksek maksimum rüzgar hızına sahip 10 şehir
df_wind = pd.read_sql_query("""
    SELECT city_name, MAX(wind_speed_10m_max) AS max_wind
    FROM daily_weather
    GROUP BY city_name
    ORDER BY max_wind DESC
    LIMIT 10
""", conn)
print("4) En yüksek maksimum rüzgar hızına sahip 10 şehir:")
print(df_wind, "\n")

conn.close()
