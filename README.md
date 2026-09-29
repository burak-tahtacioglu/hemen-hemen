# Hemen Hemen — GitHub Pages

Destek, gizlilik ve tanıtım sayfalarının bağımsız yayın klasörü.

## Önce yapılandırın

GitHub kullanıcı/depo adı, gerçek destek e-postası ve uygulama sahibi/veri sorumlusu adı gereklidir. Metinlerdeki taslak alanlar tamamlanmadan workflow yayın yapmaz.

```sh
python3 configure.py --owner KULLANICI --repo DEPO --email DESTEK_EPOSTASI --operator 'Kişi veya şirket adı'
python3 validate.py
```

`app-store-links.json` App Store Connect'e girilecek Support URL, Privacy Policy URL ve isteğe bağlı Marketing URL'yi içerir. Klasör mevcut iOS projesinin içindeyse script aynı adresleri Info.plist'e ekler.

## Yayın

1. Yalnızca bu klasörün içeriğini ayrı bir GitHub deposunun köküne yükleyin. Ana iOS projesi, API dosyaları, anahtarlar ve veritabanı dosyalarını bu depoya yüklemeyin.
2. Depo Settings → Pages → Source altında GitHub Actions seçin.
3. main dalına gönderin veya Pages workflow'unu çalıştırın.
4. Yayın tamamlandıktan sonra üç adresin HTTP 200 döndüğünü kontrol edin.
5. `support.html` adresini Support URL, `privacy.html` adresini Privacy Policy URL, ana adresi Marketing URL olarak kullanın.

Kullanıcı sitesi `KULLANICI.github.io` adlı depoda yayınlanırsa URL kökten başlar; proje deposunda depo adı URL'ye eklenir.

## İçerik

Metin mevcut uygulama akışlarına göre hazırlanmıştır. Başvuru iletişimi, veri sorumlusu kimliği ve gerçek işletme süreçleri uygulama sahibi tarafından tamamlanmalıdır. Bu genel gizlilik politikası, belirli veri toplama akışlarında gerekli olabilecek ayrı aydınlatma veya rıza metninin yerine geçmez.

Kaynaklar:
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://developer.apple.com/app-store/review/guidelines/#privacy
- https://www.kvkk.gov.tr/Icerik/6765/AYDINLATMA-YUKUMLULUGUNUN-YERINE-GETIRILMESI-HAKKINDA-KAMUOYU-DUYURUSU
