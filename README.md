🌤️ Weather Data Engineering Project

EDA • OLTP • OLAP • Roll-Up • Slice • Dice • Visualization

Bu proje, farklı şehirlerden çekilmiş günlük hava durumu verilerini kullanarak bir veri mühendisliği sürecini uçtan uca gösteren küçük bir çalışmadır. Çalışmada EDA, basit ETL, OLTP veritabanı oluşturma, OLAP analizleri ve grafik görselleştirmeleri yapılmıştır. Üniversite dersindeki içerikler temel alınmış, bazı bölümlerde AI desteğiyle düzenlemeler yapılmıştır.

📌 1. Veri Seti

Veri kaynağı: daily_data.csv
İçerik:

Şehir adı

Tarih

Maksimum sıcaklık

Minimum sıcaklık

Ortalama sıcaklık

Yağış miktarı

Hava kodu

📌 2. EDA (Exploratory Data Analysis)

Ön analiz kısmında aşağıdakiler incelendi:

Eksik veri kontrolü

Sıcaklıkların genel dağılımı

Şehirlere göre ortalama sıcaklık karşılaştırmaları

Maksimum sıcaklık değişimi

Kısa İstatistiksel Örnek (İstenen):

Örnek olarak ortalama sıcaklık için temel istatistik hesaplanmıştır:

Ortalama: df["temperature_2m_mean"].mean()

Medyan: df["temperature_2m_mean"].median()

Standart sapma: df["temperature_2m_mean"].std()

Bu değerler, verinin normal dağılıma yakın bir yapıda olduğunu göstermektedir.

📌 3. Basit ETL

Bu projede ETL kısmı sade tutulmuştur.

Extract: CSV dosyasından okuma

Transform: Gereksiz sütunların çıkarılması

Load: SQLite üzerine OLTP tabloya yükleme

Kodlar oltp.py içinde bulunmaktadır.

📌 4. OLTP Tasarımı

SQLite üzerinde daily_weather tablosu oluşturulmuştur.

Alanlar:

city_name

datetime

temperature_2m_max

temperature_2m_min

temperature_2m_mean

precipitation_sum

weather_code

Amaç: Hızlı veri ekleme ve işlem yapma.

📌 5. OLAP Tasarımı

OLAP işlemleri için tablo, daha geniş analizlere uygun hâle dönüştürülerek olap.db içinde saklanmıştır.

Yapılan OLAP işlemleri:

🔹 1) Roll-Up

Zaman boyutunda gün → ay seviyesine çıkarma
Örnek:
Aylık ortalama sıcaklık hesaplama.

🔹 2) Slice

Tek şehir seçip o şehirdeki tüm yılları analiz etme.
Örnek:
"Bangkok" için tüm zaman serisini analiz etme.

🔹 3) Dice

Birden fazla koşula göre alt küme alma.
Örnek:

Şehir: İstanbul

Yıl: 2019

Sıcaklık > 30°C

📌 6. Görselleştirme

Matplotlib ile aşağıdaki grafikler çizilmiştir:

Maksimum sıcaklık zaman serisi

Aylık ortalama sıcaklık grafiği

Yağış miktarı değişimi grafik analizleri

Grafikler /plots klasöründe yer alır.

📌 7. Dosya Yapısı
.
├── oltp.py
├── olap.py
├── analysis.ipynb
├── daily_data.csv
├── oltp.db
├── olap.db
├── plots/
│   ├── max_temp.png
│   ├── monthly_avg.png
│   └── precipitation.png
└── README.md

📌 8. Kullanım
python oltp.py
python olap.py

📌 9. Sonuç

Bu mini proje kapsamında:

Ham veri okunmuş,

OLTP veritabanına aktarılmış,

OLAP yapılandırılmış,

Roll-Up, Slice, Dice işlemleri uygulanmış,

Grafik analizleri yapılmıştır.

Ders kapsamında işlenen kavramlar pratik bir örnek üzerinde uygulanmış, bazı düzenlemelerde AI desteğinden yararlanılmıştır.
