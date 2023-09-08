
<p align="center">
Çeviriler<br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/CONTRIBUTING.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/CONTRIBUTING.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/CONTRIBUTING.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/CONTRIBUTING.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/CONTRIBUTING.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/CONTRIBUTING.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/CONTRIBUTING.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/CONTRIBUTING.md>🇨🇳 ZH   </a>
</p>


Merhaba!

Ciphey'e katkıda bulunmakla ilgileniyor musunuz? 🤔

Belki de nereden başlayacağınız konusunda kafanız karışık ya da kodlama becerilerinizin "yeterince iyi" olmadığına inanıyorsunuz? İkincisi için - bu çok saçma! "Kötü kod" ile bir sorunumuz yok ve o zaman bile bu belgeyi okuyorsanız muhtemelen harika bir programcısınız. Demek istediğim, yeni başlayanlar genellikle GitHub projelerine katkıda bulunmayı öğrenmezler 😉

İşte Ciphey'e katkıda bulunabileceğiniz bazı yollar:

- Yeni bir dil ekleyin 🧏
- Daha fazla şifreleme yöntemi ekleyin 📚
- Daha fazla dokümantasyon oluşturun (çok önemli! Sonsuza kadar minnettar oluruz)
- GitHub sorunları aracılığıyla gönderilen hataları düzeltin (bu konuda size destek olabiliriz 😊)
- Kod tabanını yeniden düzenleyin 🥺

Bunlar kulağa zor geliyorsa endişelenmeyin! Bu belge, bunlardan herhangi birini tam olarak nasıl başaracağınız konusunda size yol gösterecektir. Ayrıca, adınız Ciphey'in katkıda bulunanlar listesine eklenecek ve sonsuza dek minnettar olacağız! 🙏

Geliştiricilerle konuşabilmeniz ve yardım alabilmeniz için küçük bir Discord sohbetimiz var. Alternatif olarak, öneriniz için bir GitHub sorunu yazabilirsiniz. Discord'a eklenmek istiyorsanız, bize DM atın veya bir şekilde bize sorun.

[Discord Sunucusu](https://discord.gg/KfyRUWw)

# Nasıl katkıda bulunabilirsiniz?


Ciphey'in her zaman daha fazla şifre çözme aracına ihtiyacı vardır! Kodun ciphey'e nasıl entegre edileceğini öğrenmek için göz atın:

- <https://github.com/Ciphey/Ciphey/wiki/Adding-your-own-ciphers> basit bir öğretici için
- <https://github.com/Ciphey/Ciphey/wiki/Extending-Ciphey> bir API referansı için

Ciphey/tests/test_main.py dosyasındaki bir fonksiyonu kopyalayarak ve şifreli metni sizin şifrenizle kodlanmış bir şeyle değiştirerek bunun için bazı testler yazarsanız iyi olur. Testler eklemezseniz, muhtemelen yine de birleştireceğiz, ancak hataları teşhis etmemiz çok daha zor olacak!

Sıkı çalışmanız için sizi katkıda bulunanlar listesine ekleyeceğimizi söylemeye gerek bile yok!

# Yeni bir dil ekleyin 🧏

Varsayılan dil denetleyicisi `brandon` birden fazla dille çalışır. Şimdi, bu kulağa ürkütücü gelebilir.
Ama dürüst olmak gerekirse, tek yapmanız gereken bir sözlük almak, biraz analiz yapmak (bu konuda size yardımcı olacak kodlar yazdık), sözlükleri ve analizi bir repoya eklemek. Ve sonra `settings.yml` seçeneğini eklemek.

# Daha fazla dokümantasyon oluşturun


Dokümantasyon Ciphey'in en önemli parçasıdır. Dokümantasyon olmaması aşırı kod yükü demektir ve biz bunu istemiyoruz.

Harika dokümantasyona katkıda bulunursanız, kod katkısı yapanlarla aynı seviyede görüleceğinizi söylediğimde bana güvenin. Dokümantasyon kesinlikle hayati önem taşımaktadır.

Belge eklemenin pek çok yolu vardır.

- Koddaki doküman dizeleri
- Mevcut dokümantasyonumuzu geliştirmek (README, bu dosya, Ciphey Wiki sayfalarımız)
- Belgelerin çevrilmesi

Ve çok daha fazlası!

# Hataları düzeltin

Ciphey'in sahip olduğu tüm hataları bulmak için GitHub sorunlar sayfamızı ziyaret edin! Onları ortadan kaldırın ve katkıda bulunanlar listesine ekleneceksiniz ;)

# Kod tabanını yeniden düzenleyin

Ciphey'in tamamı PEP8'i takip etmez ve kodun bir kısmı tekrar edilir.
