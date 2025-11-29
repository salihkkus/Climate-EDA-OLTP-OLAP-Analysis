import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Veritabanına bağlan
conn = sqlite3.connect("oltp.db")

# 1) Şehirlere göre ortalama sıcaklık
df_avg_temp = pd.read_sql_query("""
    SELECT city_name, AVG(temperature_2m_max) AS avg_temp
    FROM daily_weather
    GROUP BY city_name
    ORDER BY avg_temp DESC
    LIMIT 10
""", conn)

# 2) Şehirlere göre toplam yağış
df_rain = pd.read_sql_query("""
    SELECT city_name, SUM(precipitation_sum) AS total_rain
    FROM daily_weather
    GROUP BY city_name
    ORDER BY total_rain DESC
    LIMIT 10
""", conn)

# 3) Şehirlere göre toplam güneşlenme süresi
# Eğer sunshine_duration yoksa tabloya eklememiz gerek, yoksa bunu atlayabiliriz
try:
    df_sun = pd.read_sql_query("""
        SELECT city_name, SUM(sunshine_duration) AS total_sun
        FROM daily_weather
        GROUP BY city_name
        ORDER BY total_sun DESC
        LIMIT 10
    """, conn)
except:
    df_sun = None

conn.close()

# Grafikler

# Ortalama sıcaklık
plt.figure(figsize=(10,5))
plt.bar(df_avg_temp['city_name'], df_avg_temp['avg_temp'], color='orange')
plt.xticks(rotation=45)
plt.ylabel("Ortalama Sıcaklık (°C)")
plt.title("Şehirlere Göre Ortalama Sıcaklık")
plt.tight_layout()
plt.show()

# Toplam yağış
plt.figure(figsize=(10,5))
plt.bar(df_rain['city_name'], df_rain['total_rain'], color='blue')
plt.xticks(rotation=45)
plt.ylabel("Toplam Yağış (mm)")
plt.title("Şehirlere Göre Toplam Yağış")
plt.tight_layout()
plt.show()

# Toplam güneşlenme süresi (varsa)
if df_sun is not None:
    plt.figure(figsize=(10,5))
    plt.bar(df_sun['city_name'], df_sun['total_sun'], color='yellow')
    plt.xticks(rotation=45)
    plt.ylabel("Toplam Güneş Süresi (saat)")
    plt.title("Şehirlere Göre Toplam Güneşlenme Süresi")
    plt.tight_layout()
    plt.show()
