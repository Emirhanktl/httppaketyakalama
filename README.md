<div align="center">
  <img src="https://img.shields.io/github/languages/count/emirhanktl/httppaketyakalama?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/emirhanktl/httppaketyakalama?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/emirhanktl/httppaketyakalama?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/emirhanktl/httppaketyakalama?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

Http Packet Capture
Http Paket Yakalama


HTTP packet capturing is the real-time listening and analysis of data packets of the HTTP protocol passing over the network. With this process, requests and responses sent and received during communication between the web browser and the web server can be examined.

HTTP paket yakalama, ağ üzerinde geçen HTTP protokolüne ait veri paketlerinin gerçek zamanlı olarak dinlenmesi ve analiz edilmesidir. Bu işlemle web tarayıcı ile web sunucusu arasındaki iletişimde gönderilen ve alınan istekler (request) ile yanıtlar (response) incelenebilir.



---

Features / Özellikler
Feature 1: Real-time HTTP packet capture and analysis.
Özellik 1: Gerçek zamanlı HTTP paketlerini yakalama ve analiz etme.

Feature 2: Filter HTTP traffic by methods such as GET, POST, PUT, DELETE.
Özellik 2: GET, POST, PUT, DELETE gibi HTTP metodlarına göre trafik filtreleme.

Feature 3: Extract and display HTTP headers and payload content.
Özellik 3: HTTP başlıklarını ve içerik (payload) verilerini çıkarıp gösterme.

Feature 4: Log captured HTTP requests and responses for later inspection.
Özellik 4: Yakalanan HTTP istek ve yanıtlarını kaydederek sonradan incelemeye imkan verme.

Feature 5: Detect suspicious or malformed HTTP traffic patterns.
Özellik 5: Şüpheli veya hatalı biçimlendirilmiş HTTP trafiğini tespit etme.
---



- 2320191041- Emirhan kutlu: Owner, organizer and manager of the project*
  *Emirhan Kutlu: Projenin sahibi , düzenleyen ve yöneten*

---


---

Research / Araştırmalar
Topic / Başlık	Link	Description / Açıklama
HTTP Protokolüne Giriş	researchs/http-protokol.md	Overview of HTTP structure and usage. / HTTP protokolünün yapısı ve kullanımı hakkında genel bilgi.
Scapy ile HTTP Paket Yakalama	researchs/scapy-http.md	Capturing HTTP packets using Scapy in Python. / Python'da Scapy ile HTTP paketlerini yakalama yöntemleri.
Şüpheli Trafik Tespiti Yöntemleri	researchs/supheli-trafik.md	Identifying suspicious patterns in HTTP traffic. / HTTP trafiğinde şüpheli kalıpların tespiti.
Paket Analizi ve Header İncelemesi	researchs/header-analizi.md	Analysis of HTTP headers and payload. / HTTP başlıkları ve içeriklerinin analizi.

## Installation / *Kurulum*

1.git clone https://github.com/Emirhanktl/httppaketyakalama.git
cd httppaketyakalama


2. python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. pip install -r requirements.txt

---

Run the project:
Projeyi çalıştırın:

bash
Kopyala
Düzenle
python httppaketyakalama.py
Starts real-time HTTP packet sniffing on the default network interface.
Varsayılan ağ arayüzü üzerinde gerçek zamanlı HTTP paket dinlemeyi başlatır.

Steps / Adımlar
Prepare input data / Giriş verilerini hazırlayın
This project does not require any pre-existing input files. It captures live HTTP traffic from your network interface. Ensure you have the proper permissions (you may need to run the script with administrator/root privileges).
Bu proje önceden hazırlanmış herhangi bir giriş dosyasına ihtiyaç duymaz. Ağ arayüzünüzden gerçek zamanlı HTTP trafiğini yakalar. Gerekli izinlere sahip olduğunuzdan emin olun (scripti yönetici/root olarak çalıştırmanız gerekebilir).

Run the script with arguments / Betiği argümanlarla çalıştırın
By default, the script works without arguments. To start capturing HTTP packets, run the script directly:
Varsayılan olarak betik herhangi bir argüman almadan çalışır. HTTP paketlerini yakalamaya başlamak için doğrudan çalıştırın:

bash
Kopyala
Düzenle
python httppaketyakalama.py
You can edit the script to add options like specifying a port, filtering IPs, or saving the output to a file.
Scripti düzenleyerek belirli portları filtreleme, IP adresi seçme veya çıktıyı bir dosyaya kaydetme gibi seçenekler ekleyebilirsiniz.

Check output / Çıktıyı kontrol edin
The captured HTTP packets will be printed in real-time to your terminal window. You can modify the script to save the data into a log or .txt file.
Yakalanan HTTP paketleri anlık olarak terminal ekranına yazdırılır. Dilerseniz scripti düzenleyerek verileri bir günlük (.log) ya da .txt dosyasına kaydedebilirsiniz.
---
Contributing / Katkıda Bulunma
We welcome contributions! To help, please follow these steps:
Topluluk katkılarınızı memnuniyetle karşılıyoruz! Katkıda bulunmak için lütfen aşağıdaki adımları izleyin:

Fork the repository / Depoyu Fork’layın
Fork yaparak projenin bir kopyasını kendi hesabınıza alın.

Clone your fork / Fork’unuzu Klonlayın

bash
Kopyala
Düzenle
git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git
Klonlama işlemi ile kendi bilgisayarınıza bir kopyasını oluşturun.

Create a branch / Yeni Bir Dal Oluşturun

bash
Kopyala
Düzenle
git checkout -b feature/your-feature
Özellik eklemek veya düzeltme yapmak için yeni bir branş (dal) oluşturun.

Commit changes with clear messages / Açık mesajlarla değişiklikleri commit’leyin
Yaptığınız değişiklikleri net commit mesajlarıyla kaydedin.

Push to your fork / Fork’unuza Push Edin

bash
Kopyala
Düzenle
git push origin feature/your-feature
Değişikliklerinizi GitHub’daki fork’unuza gönderin.

Open a Pull Request / Pull Request Açın
Ana projeye katkılarınızın dahil edilmesi için Pull Request oluşturun.

Follow our coding standards (see CONTRIBUTING.md).
Lütfen kodlama standartlarımıza uyun (bkz. CONTRIBUTING.md).



## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Awesome Library: For enabling X.  
- Inspiration Source.  
- Special thanks to...  

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Your Name/Org Name] - [your.email@example.com]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Adınız/Kuruluş Adınız] - [e-posta.adresiniz@ornek.com]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
