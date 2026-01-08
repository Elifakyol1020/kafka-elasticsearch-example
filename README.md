# Kafka + Elasticsearch + Kibana Final Projesi
## 📱 Sosyal Medya Akış Verileri Analiz Sistemi

Bu proje, Kafka, Elasticsearch ve Kibana kullanarak sosyal medya platform etkileşim verilerini gerçek zamanlı olarak işleyen ve analiz eden bir sistem oluşturmaktadır.

## 🎯 Proje Özellikleri

- **Kafka**: Sürekli sosyal medya veri akışı (beğeni, yorum, paylaşım, görüntülenme)
- **Elasticsearch**: Verilerin indekslenmesi ve saklanması
- **Kibana**: Gerçek zamanlı dashboard'lar ve analizler

## 📊 Veri Yapısı

Her veri kaydı şu bilgileri içerir:
- `event_id`: Benzersiz etkinlik ID'si
- `post_id`: Paylaşım ID'si
- `user_id`: Kullanıcı ID'si
- `content_type`: İçerik türü (photo, video, text, story, reel)
- `likes`: Beğeni sayısı
- `comments`: Yorum sayısı
- `shares`: Paylaşım sayısı
- `views`: Görüntülenme sayısı
- `hashtags`: Hashtag listesi
- `engagement_rate`: Etkileşim oranı (%)
- `location`: Konum (şehir)
- `is_viral`: Viral içerik mi? (true/false)
- `post_created_at`: Paylaşım oluşturulma zamanı
- `interaction_timestamp`: Etkileşim zamanı

## 📈 Yapılabilecek Analizler

- ✅ En çok beğenilen paylaşımlar
- ✅ En aktif kullanıcılar
- ✅ İçerik türü bazlı performans analizi
- ✅ Zaman bazlı etkileşim trendleri
- ✅ Viral içerik tespiti ve analizi
- ✅ Engagement rate analizi
- ✅ Konum bazlı etkileşim analizi
- ✅ İçerik türü karşılaştırmaları

---

## Veri Seti Seçenekleri (Diğer Seçenekler)

Lütfen aşağıdaki veri seti seçeneklerinden birini seçin:

### 1. 🛒 E-Ticaret Sipariş Verileri
- **Veri Türü**: Online mağaza sipariş verileri
- **Örnek Veriler**: Ürün ID, kategori, fiyat, müşteri ID, sipariş zamanı, miktar
- **Analizler**:
  - En çok sipariş verilen ürünler
  - Saatlik/günlük sipariş sayıları
  - Kategori bazlı satış analizi
  - Ortalama sipariş tutarı
  - En aktif müşteriler

### 2. 🌡️ IoT Sensör Verileri
- **Veri Türü**: Akıllı bina/şehir sensör verileri
- **Örnek Veriler**: Sensör ID, sıcaklık, nem, basınç, konum, zaman damgası
- **Analizler**:
  - Anomali tespiti (normal değer aralığı dışındaki veriler)
  - Sensör bazlı ortalama değerler
  - Zaman bazlı trend analizi
  - En yüksek/düşük değerler
  - Konum bazlı sensör performansı

### 3. 📱 Sosyal Medya Akış Verileri
- **Veri Türü**: Sosyal medya platform etkileşim verileri
- **Örnek Veriler**: Post ID, beğeni sayısı, yorum sayısı, paylaşım sayısı, kullanıcı ID, içerik türü
- **Analizler**:
  - En çok beğenilen paylaşımlar
  - En aktif kullanıcılar
  - İçerik türü bazlı performans
  - Zaman bazlı etkileşim trendleri
  - Viral içerik tespiti

### 4. 🚗 Trafik Verileri
- **Veri Türü**: Gerçek zamanlı trafik akış verileri
- **Örnek Veriler**: Konum (lat/long), hız, araç sayısı, yol adı, zaman damgası
- **Analizler**:
  - En yoğun trafik saatleri
  - En yoğun bölgeler/yollar
  - Ortalama hız analizi
  - Trafik yoğunluğu haritası
  - Zaman bazlı trafik trendleri

### 5. 💳 Bankacılık İşlem Verileri
- **Veri Türü**: Finansal işlem kayıtları
- **Örnek Veriler**: İşlem ID, işlem türü, tutar, hesap ID, zaman damgası, işlem durumu
- **Analizler**:
  - İşlem türü bazlı dağılım
  - Saatlik/günlük işlem hacmi
  - Ortalama işlem tutarı
  - En aktif hesaplar
  - Şüpheli işlem tespiti (yüksek tutarlı işlemler)

## Proje Yapısı

```
bigdatafinalproject/
├── docker-compose.yml          # Kafka, Elasticsearch, Kibana servisleri
├── producer/                    # Kafka producer (veri üretici)
│   ├── requirements.txt
│   └── producer.py
├── consumer/                   # Kafka consumer (Elasticsearch'e yazıcı)
│   ├── requirements.txt
│   └── consumer.py
├── data/                       # Veri setleri (seçime göre)
└── README.md
```

## 🚀 Kurulum ve Çalıştırma

### 1. Gereksinimler

- Docker ve Docker Compose
- Python 3.8+
- pip

### 2. Servisleri Başlatma

Docker Compose ile tüm servisleri (Kafka, Zookeeper, Elasticsearch, Kibana) başlatın:

```bash
docker-compose up -d
```

Servislerin durumunu kontrol edin:
```bash
docker-compose ps
```

Servislerin hazır olması 1-2 dakika sürebilir. Özellikle Elasticsearch ve Kibana'nın tamamen başlamasını bekleyin.

### 3. Veri Üreticisini (Producer) Çalıştırma

Yeni bir terminal açın ve producer'ı başlatın:

```bash
cd producer
pip install -r requirements.txt
python producer.py
```

Producer her 2 saniyede bir sosyal medya verisi üretecek ve Kafka'ya gönderecektir.

### 4. Veri Tüketicisini (Consumer) Çalıştırma

Başka bir terminal açın ve consumer'ı başlatın:

```bash
cd consumer
pip install -r requirements.txt
python consumer.py
```

Consumer, Kafka'dan verileri okuyup Elasticsearch'e yazacaktır.

### 5. Kibana'ya Erişim

Tarayıcınızda şu adrese gidin:
```
http://localhost:5601
```

**Önemli**: Kibana'nın tamamen başlaması 2-3 dakika sürebilir. İlk açılışta "Kibana is starting" mesajını görebilirsiniz.

### 6. Kibana Dashboard Kurulumu

Detaylı kurulum talimatları için `KIBANA_SETUP.md` dosyasına bakın.

Kısa özet:
1. Stack Management → Index Patterns → `social-media-events` oluştur
2. Time field: `interaction_timestamp` seç
3. Visualize Library'de visualization'lar oluştur
4. Dashboard'a ekle

## 📚 Dokümantasyon

- **KIBANA_SETUP.md**: Kibana dashboard kurulum ve analiz kılavuzu
- **README.md**: Bu dosya

## 🔧 Servis Portları

- **Kafka**: `localhost:9092`
- **Zookeeper**: `localhost:2181`
- **Elasticsearch**: `localhost:9200`
- **Kibana**: `localhost:5601`

## 🛑 Servisleri Durdurma

```bash
docker-compose down
```

Verileri de silmek için:
```bash
docker-compose down -v
```

## 📝 Notlar

- Producer ve Consumer'ı aynı anda çalıştırmanız gerekir.
- İlk verilerin Elasticsearch'e yazılması birkaç saniye sürebilir.
- Kibana'da index pattern oluşturduktan sonra veriler görünür hale gelir.
- Dashboard'ları düzenli olarak yenileyin (Refresh butonu).
- Producer'ı durdurduğunuzda veri akışı durur, ancak mevcut veriler Elasticsearch'te kalır.

## 🐛 Sorun Giderme

### Elasticsearch bağlantı hatası:
- Elasticsearch'in tamamen başladığından emin olun: `curl http://localhost:9200`
- Birkaç dakika bekleyip tekrar deneyin.

### Kafka bağlantı hatası:
- Kafka ve Zookeeper'ın çalıştığını kontrol edin: `docker-compose ps`
- Producer ve Consumer'ı yeniden başlatın.

### Kibana'da veri görünmüyor:
- Index pattern'in doğru oluşturulduğundan emin olun.
- Time field'in `interaction_timestamp` olduğunu kontrol edin.
- Zaman filtresini genişletin (son 7 gün, son 30 gün vb.).

