
# Repository Evaluation

- Python files present: Yes (10/10)
- readme.md present: Yes (10/10)
- researchs folder with at least 2 .md files: Yes (20/20)
- researchs folder with at least 1 .pdf file: Yes (10/10)
- requirements.txt present: Yes (10/10)
- Python code quality and logic: 30/40

## Code Review (in Turkish)
Kod Değerlendirme Raporu:

1. Okunabilirlik (12/15 puan):
- Fonksiyon ve değişken isimleri anlaşılır ve Türkçe kullanılmış
- Temel açıklayıcı yorumlar mevcut
- PEP 8 stil kurallarına genel olarak uyulmuş
- Daha detaylı fonksiyon açıklamaları (docstring) eklenebilirdi
- Hata yakalama ve loglama mekanizmaları eksik

2. Yapı (7/10 puan):
- Kod modüler yapıda ve fonksiyonlara ayrılmış
- Main fonksiyonu ve program giriş noktası doğru tanımlanmış
- İki boş app.py dosyası gereksiz duruyor
- Konfigürasyon ayarları ayrı bir dosyada tutulabilirdi
- Paket yakalama fonksiyonu daha küçük parçalara bölünebilirdi

3. Mantık (11/15 puan):
- Scapy kütüphanesi kullanılarak HTTP paketlerini yakalama mantığı doğru
- TCP ve Raw katman kontrolü yapılıyor
- Sadece port 80 dinleniyor, HTTPS (443) desteği yok
- Hata durumları ele alınmamış
- Performans için paket filtreleme optimize edilebilir
- Yakalanan paketlerin kaydedilmesi veya analizi için ek özellikler eklenebilir

Toplam Puan: 30/40

Öneriler:
- Hata yakalama mekanizmaları eklenmeli
- HTTPS desteği eklenebilir
- Daha detaylı dokümantasyon yazılmalı
- Konfigürasyon ayarları ayrı bir dosyaya alınmalı
- Gereksiz boş dosyalar kaldırılmalı
- Paket analizi için daha detaylı fonksiyonlar eklenebilir
- Yakalanan paketlerin kaydedilmesi için bir mekanizma eklenebilir

Kod temel işlevselliği sağlamakla birlikte, üretim ortamı için geliştirilmesi gereken yönleri bulunmaktadır.

Total Score: 90/100
