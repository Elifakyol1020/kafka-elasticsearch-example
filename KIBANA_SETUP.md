# Kibana Dashboard Kurulum ve Analiz Kılavuzu

Bu dokümantasyon, sosyal medya akış verileri için Kibana dashboard'unun nasıl kurulacağını ve hangi analizlerin yapılabileceğini açıklar.

## 1. Kibana'ya Erişim

1. Docker servislerinin çalıştığından emin olun:
```bash
docker-compose ps
```

2. Tarayıcınızda şu adrese gidin:
```
http://localhost:5601
```

3. İlk açılışta birkaç dakika beklemeniz gerekebilir (Kibana başlatılıyor).

## 2. Index Pattern Oluşturma

1. Kibana'da sol menüden **"Stack Management"** (⚙️) seçeneğine tıklayın.
2. **"Index Patterns"** seçeneğine tıklayın.
3. **"Create index pattern"** butonuna tıklayın.
4. Index pattern olarak `social-media-events` yazın ve **"Next step"** butonuna tıklayın.
5. Time field olarak **"interaction_timestamp"** seçin.
6. **"Create index pattern"** butonuna tıklayın.

## 3. Discover ile Veri Görüntüleme

1. Sol menüden **"Discover"** (🔍) seçeneğine tıklayın.
2. Index pattern olarak `social-media-events` seçin.
3. Verilerinizi görebilir ve filtreleyebilirsiniz.

## 4. Dashboard Oluşturma

### 4.1. En Çok Beğenilen Paylaşımlar

1. Sol menüden **"Visualize Library"** (📊) seçeneğine tıklayın.
2. **"Create visualization"** butonuna tıklayın.
3. **"Data Table"** seçeneğini seçin.
4. Index pattern olarak `social-media-events` seçin.
5. **Metrics** bölümünde:
   - Aggregation: **Top values**
   - Field: **post_id.keyword**
   - Size: **10**
6. **Buckets** bölümünde:
   - Add bucket → **Split rows**
   - Aggregation: **Terms**
   - Field: **post_id.keyword**
   - Size: **10**
   - Order by: **Metric: Top values**
   - Order: **Descending**
7. **Metrics** bölümünde (buckets içinde):
   - Aggregation: **Sum**
   - Field: **likes**
8. **"Save"** butonuna tıklayın ve isim verin: **"Top 10 Most Liked Posts"**

### 4.2. İçerik Türü Bazlı Performans

1. Yeni bir visualization oluşturun, **"Vertical Bar"** seçin.
2. **Metrics** bölümünde:
   - Aggregation: **Average**
   - Field: **likes**
3. **Buckets** bölümünde:
   - Add bucket → **X-axis**
   - Aggregation: **Terms**
   - Field: **content_type.keyword**
   - Order by: **Metric: Average likes**
   - Order: **Descending**
4. **"Save"** butonuna tıklayın: **"Content Type Performance"**

### 4.3. Zaman Bazlı Etkileşim Trendleri

1. Yeni bir visualization oluşturun, **"Line"** seçin.
2. **Metrics** bölümünde:
   - Aggregation: **Sum**
   - Field: **likes**
3. **Buckets** bölümünde:
   - Add bucket → **X-axis**
   - Aggregation: **Date Histogram**
   - Field: **interaction_timestamp**
   - Interval: **1 hour** (veya istediğiniz aralık)
4. **"Save"** butonuna tıklayın: **"Likes Over Time"**

### 4.4. En Aktif Kullanıcılar

1. Yeni bir visualization oluşturun, **"Data Table"** seçin.
2. **Metrics** bölümünde:
   - Aggregation: **Count**
3. **Buckets** bölümünde:
   - Add bucket → **Split rows**
   - Aggregation: **Terms**
   - Field: **user_id.keyword**
   - Size: **20**
   - Order by: **Metric: Count**
   - Order: **Descending**
4. **"Save"** butonuna tıklayın: **"Top 20 Active Users"**

### 4.5. Viral İçerik Analizi

1. Yeni bir visualization oluşturun, **"Pie"** seçin.
2. **Metrics** bölümünde:
   - Aggregation: **Count**
3. **Buckets** bölümünde:
   - Add bucket → **Split slices**
   - Aggregation: **Terms**
   - Field: **is_viral**
   - Size: **2**
4. **"Save"** butonuna tıklayın: **"Viral vs Non-Viral Content"**

### 4.6. Engagement Rate Analizi

1. Yeni bir visualization oluşturun, **"Metric"** seçin.
2. **Metrics** bölümünde:
   - Aggregation: **Average**
   - Field: **engagement_rate**
   - Custom label: **"Average Engagement Rate (%)"**
3. **"Save"** butonuna tıklayın: **"Average Engagement Rate"**

### 4.7. Konum Bazlı Analiz

1. Yeni bir visualization oluşturun, **"Tag Cloud"** seçin.
2. **Metrics** bölümünde:
   - Aggregation: **Sum**
   - Field: **likes**
3. **Buckets** bölümünde:
   - Add bucket → **Tags**
   - Aggregation: **Terms**
   - Field: **location.keyword**
   - Size: **15**
   - Order by: **Metric: Sum of likes**
   - Order: **Descending**
4. **"Save"** butonuna tıklayın: **"Top Locations by Likes"**

### 4.8. İçerik Türü Karşılaştırması (Beğeni, Yorum, Paylaşım)

1. Yeni bir visualization oluşturun, **"Vertical Bar"** seçin.
2. **Metrics** bölümünde:
   - Aggregation: **Average**
   - Field: **likes**
   - Custom label: **"Avg Likes"**
   - Add metric:
     - Aggregation: **Average**
     - Field: **comments**
     - Custom label: **"Avg Comments"**
   - Add metric:
     - Aggregation: **Average**
     - Field: **shares**
     - Custom label: **"Avg Shares"**
3. **Buckets** bölümünde:
   - Add bucket → **X-axis**
   - Aggregation: **Terms**
   - Field: **content_type.keyword**
4. **"Save"** butonuna tıklayın: **"Content Type Comparison"**

## 5. Dashboard Oluşturma

1. Sol menüden **"Dashboard"** (📈) seçeneğine tıklayın.
2. **"Create dashboard"** butonuna tıklayın.
3. **"Add"** butonuna tıklayın ve oluşturduğunuz tüm visualization'ları ekleyin.
4. Visualization'ları sürükleyip bırakarak düzenleyin.
5. **"Save"** butonuna tıklayın ve dashboard'a bir isim verin: **"Social Media Analytics Dashboard"**

## 6. Örnek KQL (Kibana Query Language) Sorguları

Discover sayfasında filtreleme için kullanabileceğiniz örnek sorgular:

### Viral içerikleri göster:
```
is_viral: true
```

### Belirli bir içerik türünü filtrele:
```
content_type: "video"
```

### Yüksek beğeni sayısına sahip postlar:
```
likes > 5000
```

### Belirli bir şehirdeki etkileşimler:
```
location: "İstanbul"
```

### Yüksek engagement rate'e sahip içerikler:
```
engagement_rate > 5
```

### Belirli bir zaman aralığı:
```
interaction_timestamp >= "2024-01-01" and interaction_timestamp <= "2024-01-31"
```

## 7. Önerilen Analizler

### A. En Çok Beğenilen Paylaşımlar
- Hangi postlar en çok beğeni aldı?
- Bu postların içerik türleri neler?
- Hangi kullanıcılar en popüler içerikleri üretiyor?

### B. En Aktif Kullanıcılar
- Hangi kullanıcılar en çok etkileşim alıyor?
- Bu kullanıcıların içerik türü tercihleri neler?

### C. İçerik Türü Bazlı Performans
- Hangi içerik türü (photo, video, text, story, reel) en çok etkileşim alıyor?
- İçerik türlerinin ortalama beğeni, yorum, paylaşım sayıları nedir?

### D. Zaman Bazlı Etkileşim Trendleri
- Hangi saatlerde en çok etkileşim oluyor?
- Günlük/haftalık trendler nasıl?

### E. Viral İçerik Tespiti
- Viral içeriklerin yüzdesi nedir?
- Viral içeriklerin ortak özellikleri neler?

### F. Engagement Rate Analizi
- Ortalama engagement rate nedir?
- Hangi içerik türleri daha yüksek engagement rate'e sahip?

### G. Konum Bazlı Analiz
- Hangi şehirlerden en çok etkileşim geliyor?
- Şehir bazlı ortalama beğeni sayıları nedir?

## 8. İpuçları

- Dashboard'ları düzenli olarak güncelleyin (Refresh butonu).
- Zaman filtrelerini kullanarak belirli dönemleri analiz edin.
- Visualization'ları export edebilirsiniz (PNG, PDF).
- Saved searches oluşturarak sık kullandığınız filtreleri kaydedin.

