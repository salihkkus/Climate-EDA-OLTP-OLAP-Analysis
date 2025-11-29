import pandas as pd

# CSV dosyasını oku
df = pd.read_csv(r"C:\Users\Salih\Desktop\OLAP+OLTP+EDA")

# İlk 5 satırı göster
print(df.head())

# Sütunları göster
print(df.columns)

# Veri tipi ve eksik değer kontrolü
print(df.info())

# Temel istatistikler
print(df.describe())
