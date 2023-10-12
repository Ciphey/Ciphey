
<p align="center">
Çeviriler <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/fr/README.md>🇫🇷 FR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/README.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/README.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/README.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/README.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/README.md>🇨🇳 ZH   </a>
 <br><br>
➡️
<a href="https://github.com/Ciphey/Ciphey/wiki">Dokümantasyon</a> |
<a href="https://discord.gg/zYTM3rZM4T">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Kurulum Rehberi</a>
 ⬅️

<br>
  <img src="../../Pictures_for_README/binoculars.png" alt="Ciphey">
</p>

<p align="center">
<img src="https://pepy.tech/badge/ciphey">
 <img src="https://pepy.tech/badge/ciphey/month">
  <a href="https://discord.gg/zYTM3rZM4T"><img alt="Discord" src="https://img.shields.io/discord/754001738184392704"></a>
<a href="https://pypi.org/project/ciphey/"><img src="https://img.shields.io/pypi/v/ciphey.svg"></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Ciphey">

<br>
Doğal dil işleme ve yapay zeka kullanan tam otomatik şifre çözme aracı.
</p>
<hr>

## [Kurulum Rehberi](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://hub.docker.com/r/remnux/ciphey">🐋 Docker (Universal) | <p align="center"><a href="https://ports.macports.org/port/ciphey/summary">🍎 MacPorts (macOS) | <p align="center"><a href="https://formulae.brew.sh/formula/ciphey">🍺 Homebrew (macOS/Linux) |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |--------------------------------------------------------------------------------- |
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p>    | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/macports.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/homebrew.png" /></p> |
| `python3 -m pip install ciphey --upgrade` | `docker run -it --rm remnux/ciphey` | `sudo port install ciphey` | `brew install ciphey` |

| Linux                                                                                                                   | Mac OS                                                                                                                     | Windows                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |

<hr>

# 🤔 Bu nedir?

Şifrelenmiş metni girin, şifresi çözülmüş şekilde metni geri alın.

> "Ne tür bir şifreleme?"

Mesele de bu zaten. Bilmiyorsun, sadece muhtemelen şifreli olduğunu biliyorsun. Ciphey bunu sizin için çözecektir.

Ciphey çoğu şeyi 3 saniye veya daha kısa sürede çözebilir.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

Ciphey, çoklu temel kodlamalar, klasik şifreler, hashler veya daha gelişmiş kriptografi gibi birçok şifre çözme ve kod çözme işlemini otomatikleştirmek için bir araç olmayı amaçlamaktadır.

Kriptografi hakkında fazla bilginiz yoksa veya üzerinde çalışmadan önce şifreli metni hızlıca kontrol etmek istiyorsanız, Ciphey tam size göre.

**Teknik kısım.** Ciphey, bir şeyin ne ile şifrelendiğini yaklaşık olarak tahmin etmek için bir _Şifre Algılama Arayüzü_ ile özel olarak oluşturulmuş bir yapay zeka modülü (_AuSearch_) kullanır. Ve ardından, verilen metnin ne zaman düz metin haline geldiğini tespit edebilen özel olarak oluşturulmuş, özelleştirilebilir bir doğal dil işleme  _Dil Denetleyici Arayüzü_ kullanır.

Burada sinir ağları veya şişirilmiş yapay zeka yok. Sadece hızlı ve minimal olanı kullanıyoruz.

Ve bu sadece buzdağının görünen kısmı. Tam teknik açıklama için şu yazımıza göz atın [dokümantasyon](https://github.com/Ciphey/Ciphey/wiki).

# ✨ Özellikler


- İkili, Mors kodu ve Base64 gibi **50'den fazla şifreleme/kodlama destekler**. Sezar şifresi, Affine şifresi ve Vigenere şifresi gibi klasik şifreleri çözebilir. Yinelenen anahtar XOR ve daha fazlası gibi modern şifreleme teknikleri de çözebildiklerine dahildir. **[Tam liste için buraya tıklayın](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**

- ** "Hangi şifreleme kullanıldı? "** sorusunu yanıtlamak için Artırılmış Arama **(AuSearch)** ile Özel Yapılmış Yapay Zeka, şifre çözme işlemlerinin 3 saniyeden daha kısa sürmesiyle sonuçlanır.
- **Özel yapım doğal dil işleme modülü** Ciphey bir şeyin düz metin olup olmadığını belirleyebilir. Bu düz metin ister JSON, ister CTF bayrağı veya İngilizce olsun, Ciphey bunu birkaç milisaniye içinde elde edebilir.
- **Çoklu Dil Desteği** şu anda sadece Almanca ve İngilizce (AU, UK, CAN, USA seçenekleriyle).
- CyberChef Magic gibi alternatiflerin desteklemediği **şifrelemeleri ve hashleri** destekler.
- **[C++ core](https://github.com/Ciphey/CipheyCore)** ile inanılmaz hızlı.

# 🔭 Ciphey vs CyberChef

## 🔁 42 kez Base64 Kodlaması çözümü karşılaştırması

<table>
  <tr>
  <th>İsim</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Zaman</th>
    <td>2 saniye</td>
    <td>6 saniye</td>
  </tr>
    <tr>
  <th>Kurulum</th>
    <td><ul><li>Ciphey'i çalıştırın</li></ul></td>
    <td><ul><li>Regex parametresin "{" şeklinde ayarlayın</li><li>Kaç kez tekrar arayacağınızı bilmeniz gerekir</li><li>Tamamının Base64 olduğunu bilmen gerek</li><li>CyberChef'i yüklemeniz gerekir (şişirilmiş bir JS uygulamasıdır)</li><li>CyberChef hakkında bu işlem sıralamasını oluşturacak kadar bilgi sahibi olmak gerekir</li><li>Eşleşmeyi ters çevirin</li></ul></td>
  </tr>
</table>

<sub><b>Not:</b> Gifler farklı zamanlarda yüklenebilir, bu nedenle biri diğerinden önemli ölçüde daha hızlı görünebilir.</sub><br>
<sub><b>Ufak bir not daha: </b>CyberChef'in Ciphey'e en çok benzeyen özelliği Magic'tir.Magic bu girdide anında başarısız oluyor ve çöküyor. CyberChef'i rekabet etmeye zorlayabilmemizin tek yolu onu manuel olarak tanımlamaktı.</sub>

CyberChef ve Ciphey'i **6gb'lık bir dosya** ile de test ettik. Ciphey dosyayı **5 dakika 54 saniye** içinde çözdü.CyberChef daha başlamadan çöktü.

## 📊 Ciphey vs Katana vs CyberChef Magic

| **İsim**                                   | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ------------ | ------------ | --------------------- |
| Gelişmiş Dil Denetleyicisi                 | ✅           | ❌           | ✅                    |
| Şifreleme Desteği                          | ✅           | ✅           | ❌                    |
| Adını Distopik temalardan alır        🌃   | ✅           | ❌           | ❌                    |
| Hash desteği                               | ✅           | ✅           | ❌                    |
| Kolay kurulum                              | ✅           | ❌           | ✅                    |
| Nasıl şifrelendiğini tahmin edebilir       | ✅           | ❌           | ❌                    |
| Hackerlar için hackerlar yaptı             | ✅           | ✅           | ❌                    |

# 🎬 Başlarken

Ciphey'i kurmakta sorun yaşıyorsanız [tıklayın](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Önemli Bağlantılar (Dokümanlar, Kurulum kılavuzu, Discord Desteği)

| Kurulum Kılavuzu                                                          | Dokümantasyon                                             | Discord                                     | Docker İmajı (REMnux'tan)                                                                         |
| --------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 📖 [Kurulum Kılavuzu ](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Dokümantasyon](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.gg/zYTM3rZM4T) | 🐋 [Docker Dokümantasyonu](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey) |

## 🏃‍♀️Ciphey'i çalıştırmak

Ciphey'i çalıştırmanın 3 yolu vardır.

1. Dosya seçimi ile `ciphey -f encrypted.txt`
2. Direkt veri girişi ile `ciphey -- "Encrypted input"`
3. Normal yol `ciphey -t "Encrypted input"`

![Gif showing 3 ways to run Ciphey](https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/3ways.gif)

İlerleme çubuklarından, olasılık tablosundan ve tüm karmaşadan kurtulmak için sessiz modu kullanın.

`ciphey -t "encrypted text here" -q`

Seçeneklerin tam listesi için `ciphey --help`.

### ⚗️ Ciphey'i kendiniz için kullanmak

Ciphey'in \main'ini içe aktarabilir ve kendi programlarınızda ve kodlarınızda kullanabilirsiniz. `from Ciphey.__main__ import main`

# 🎪 Katkıda Bulunanlar


Ciphey, 2008 yılında [Bee](https://github.com/bee-san) tarafından icat edildi ve 2019 yılında yeniden hayata geçirildi. Ciphey, UoL Siber Güvenlik Topluluğu başkanı [Cyclic3](https://github.com/Cyclic3) olmasaydı bugün olduğu yerde olamazdı.

Ciphey, CTF'lerde kullanılmak üzere [Cyber Security Society](https://www.cybersoc.cf/) tarafından yeniden hayata geçirildi ve yeniden oluşturuldu. Liverpool'a yolunuz düşerse, bir konuşma yapmayı ya da etkinliklerimize sponsor olmayı düşünün. Daha fazla bilgi edinmek için `cybersecurity@society.liverpoolguild.org` adresinden bize e-posta gönderin 🤠

Arama sürecini hızlandırmak için uygun algoritmaları nasıl kullanabileceğimizi bulduğu için George H'ye **teşekkürler**
Logo tasarımı için [varghalladesign](https://www.facebook.com/varghalladesign)'a **teşekkürler**. Diğer tasarım çalışmalarına göz atın!




## 🐕‍🦺 [Katkıda Bulunmak](https://github.com/Ciphey/Ciphey/wiki/Contributing)


Katkıda bulunmaktan korkmayın! Yardım etmek için yapabileceğiniz pek çok şey var. Her biri etiketlenmiş ve örneklerle kolayca açıklanmıştır. Katkıda bulunmaya çalışıyor ancak takılıyorsanız, @bee-san'ı etiketleyin ✨

Alternatif olarak, Discord grubuna katılın ve oraya bir mesaj gönderin ([katkıda Bulunma dosyası](https://github.com/Ciphey/Ciphey/wiki/Contributing) içindeki bağlantı) veya bu README'nin üst kısmında bir rozet olarak.

Nasıl katkıda bulunacağınızla ilgili tam ayrıntılar için lütfen [katkıda bulunma dosyası](https://github.com/Ciphey/Ciphey/wiki/Contributing) adresini okuyun ✨

Bunu yaparak, adınızı aşağıdaki README'ye ekletecek ve sürekli büyüyen bir projenin parçası olacaksınız!



## 💰 Maddi Katkıda Bulunanlar


Katkılar sadece Ciphey ve yazarlarının geleceğini değil, aynı zamanda Liverpool Üniversitesi'ndeki Siber Güvenlik Topluluğu'nu da finanse etmek için kullanılacak.

GitHub "bu projeye sponsor olun ve parayı eşit olarak dağıtalım" seçeneğini desteklemiyor, bu nedenle bağış yaparsanız biz kendi aramızda hallederiz 🥰

## ✨ Katkı Sağlayanlar

Bu harika insanlara teşekkür ederiz ([Emoji Anahtarı ✨ (ve Katkı Tipleri)](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Cyclic3"><img src="https://avatars1.githubusercontent.com/u/15613874?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cyclic3</b></sub></a><br /><a href="#design-cyclic3" title="Design">🎨</a> <a href="#maintenance-cyclic3" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=cyclic3" title="Code">💻</a> <a href="#ideas-cyclic3" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://skerritt.blog"><img src="https://avatars3.githubusercontent.com/u/10378052?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Brandon</b></sub></a><br /><a href="#design-brandonskerritt" title="Design">🎨</a> <a href="#maintenance-brandonskerritt" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=brandonskerritt" title="Code">💻</a> <a href="#ideas-brandonskerritt" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/michalani"><img src="https://avatars0.githubusercontent.com/u/27767884?v=4?s=100" width="100px;" alt=""/><br /><sub><b>michalani</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=michalani" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ashb07"><img src="https://avatars2.githubusercontent.com/u/24845568?v=4?s=100" width="100px;" alt=""/><br /><sub><b>ashb07</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=ashb07" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/TheAlcanian"><img src="https://avatars3.githubusercontent.com/u/22127191?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Shardion</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ATheAlcanian" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/Bryzizzle"><img src="https://avatars0.githubusercontent.com/u/57810197?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bryan</b></sub></a><br /><a href="#translation-Bryzizzle" title="Translation">🌍</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=Bryzizzle" title="Documentation">📖</a></td>
    <td align="center"><a href="https://lukasgabriel.net"><img src="https://avatars0.githubusercontent.com/u/52338810?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Lukas Gabriel</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=lukasgabriel" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Alukasgabriel" title="Bug reports">🐛</a> <a href="#translation-lukasgabriel" title="Translation">🌍</a> <a href="#ideas-lukasgabriel" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/DarshanBhoi"><img src="https://avatars2.githubusercontent.com/u/70128281?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Darshan</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ADarshanBhoi" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/SkeletalDemise"><img src="https://avatars1.githubusercontent.com/u/29117662?v=4?s=100" width="100px;" alt=""/><br /><sub><b>SkeletalDemise</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=SkeletalDemise" title="Code">💻</a></td>
    <td align="center"><a href="https://www.patreon.com/cclauss"><img src="https://avatars3.githubusercontent.com/u/3709715?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Christian Clauss</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=cclauss" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Acclauss" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://machinexa.xss.ht"><img src="https://avatars1.githubusercontent.com/u/60662297?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Machinexa2</b></sub></a><br /><a href="#content-machinexa2" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/anantverma275"><img src="https://avatars1.githubusercontent.com/u/18184503?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Anant Verma</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=anantverma275" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Aanantverma275" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/XVXTOR"><img src="https://avatars1.githubusercontent.com/u/40268197?v=4?s=100" width="100px;" alt=""/><br /><sub><b>XVXTOR</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=XVXTOR" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Itamikame"><img src="https://avatars2.githubusercontent.com/u/59034423?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Itamikame</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Itamikame" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/MikeMerz"><img src="https://avatars3.githubusercontent.com/u/50526795?v=4?s=100" width="100px;" alt=""/><br /><sub><b>MikeMerz</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=MikeMerz" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jacobggman"><img src="https://avatars2.githubusercontent.com/u/30216976?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jacob Galam</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=jacobggman" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Ajacobggman" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://tuxthexplorer.github.io/"><img src="https://avatars1.githubusercontent.com/u/37508897?v=4?s=100" width="100px;" alt=""/><br /><sub><b>TuxTheXplorer</b></sub></a><br /><a href="#translation-TuxTheXplorer" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/Itamai"><img src="https://avatars3.githubusercontent.com/u/53093696?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Itamai</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Itamai" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3AItamai" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/Termack"><img src="https://avatars2.githubusercontent.com/u/26333901?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Filipe</b></sub></a><br /><a href="#translation-Termack" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/malathit"><img src="https://avatars0.githubusercontent.com/u/2684148?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Malathi</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=malathit" title="Code">💻</a></td>
    <td align="center"><a href="https://hexchaos.xyz/"><img src="https://avatars1.githubusercontent.com/u/8947820?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jack</b></sub></a><br /><a href="#translation-HexChaos" title="Translation">🌍</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/yafkari"><img src="https://avatars3.githubusercontent.com/u/41365655?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Younes</b></sub></a><br /><a href="#translation-yafkari" title="Translation">🌍</a></td>
    <td align="center"><a href="https://gitlab.com/Marnick39"><img src="https://avatars2.githubusercontent.com/u/17315511?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Marnick Vandecauter</b></sub></a><br /><a href="#translation-Marnick39" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/mav8557"><img src="https://avatars0.githubusercontent.com/u/47306745?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Michael V</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=mav8557" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/chuinzer"><img src="https://avatars2.githubusercontent.com/u/64257785?v=4?s=100" width="100px;" alt=""/><br /><sub><b>chuinzer</b></sub></a><br /><a href="#translation-chuinzer" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/blackcat-917"><img src="https://avatars1.githubusercontent.com/u/53786619?v=4?s=100" width="100px;" alt=""/><br /><sub><b>blackcat-917</b></sub></a><br /><a href="#translation-blackcat-917" title="Translation">🌍</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=blackcat-917" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Ozzyz"><img src="https://avatars3.githubusercontent.com/u/6113447?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Åsmund Brekke</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Ozzyz" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/sashreek1"><img src="https://avatars1.githubusercontent.com/u/45600974?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sashreek Shankar</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=sashreek1" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/cryptobadger"><img src="https://avatars2.githubusercontent.com/u/26308101?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cryptobadger</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=cryptobadger" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Acryptobadger" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/e1fy"><img src="https://avatars3.githubusercontent.com/u/61194758?v=4?s=100" width="100px;" alt=""/><br /><sub><b>elf</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=e1fy" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/rogercyyu"><img src="https://avatars0.githubusercontent.com/u/45835736?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Roger Yu</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=rogercyyu" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/JesseEmond"><img src="https://avatars.githubusercontent.com/u/1843555?v=4?s=100" width="100px;" alt=""/><br /><sub><b>dysleixa</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=JesseEmond" title="Code">💻</a></td>
    <td align="center"><a href="http://mohzulfikar.me"><img src="https://avatars.githubusercontent.com/u/48849323?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mohammad Zulfikar</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=mohzulfikar" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/AABur"><img src="https://avatars.githubusercontent.com/u/41373199?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexander Burchenko</b></sub></a><br /><a href="#translation-AABur" title="Translation">🌍</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

Bu proje [katkıda bulunanlar](https://github.com/all-contributors/all-contributors) özelliğini takip etmektedir. Her türlü katkıya açığız!
