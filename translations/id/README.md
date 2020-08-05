<p align="center">
➡️ 
<a href="https://docs.ciphey.online">Dokumentasi</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://docs.ciphey.online/en/latest/install.html">Petunjuk Instalasi</a>
 ⬅️

<br>
  <img src="Pictures_for_README/binoculars.png" alt="Ciphey">
</p>

<p align="center">
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/ciphey/ciphey">
<img src="https://pepy.tech/badge/ciphey">
 <img src="https://pepy.tech/badge/ciphey/month">
  <a href="https://discord.gg/wM3scnc"><img alt="Discord" src="https://img.shields.io/discord/728245678895136898"></a>
<a href="https://pypi.org/project/ciphey/"><img src="https://img.shields.io/pypi/v/ciphey.svg"></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Ciphey">
  
  <img src="https://github.com/brandonskerritt/Ciphey/workflows/Python%20application/badge.svg?branch=master" alt="Ciphey">
<br>
Alat dekripsi otomatis yang menggunakan pemrosesan bahasa alami & kecerdasan buatan, bersama dengan beberapa akal sehat.
</p>
<hr>

## [Petunjuk Instalasi](https://docs.ciphey.online/en/latest/install.html)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python (Universal) </a></p> |
| ----------------------------------------------------------------------------------------- |
| <p align="center"><img src="Pictures_for_README/python.png" /></p>                        |                       |
| `python3 -m pip install ciphey --upgrade`                                                 | 

| Linux       | Mac OS | Windows     |
| ----------- | ------ | ----------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) |![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |
  

<hr>

# 🤔 Apa itu Ciphey?
Ciphey adalah sebuah alat dekripsi otomatis. Masukkan teks terenkripsi, dapatkan kembali teks yang didekripsi
> "Jenis enkripsi apa?"

Itulah intinya. Anda tidak tahu, Anda hanya tahu itu mungkin dienkripsi. Ciphey akan mencari tahu untuk Anda.

Ciphey dapat mendekripsi kebanyakan hal dalam 3 detik atau kurang.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

**Detail teknis** Ciphey mengunakan modul kecerdasan buatan (_AuSearch_) dengan sebuah _Antarmuka Deteksi Cipher_ untuk memperkirakan enkripsi teks yang diberikan. Dan kemudian, sebuah _Antarmuka Pemerika Bahasa_ yang dibuat khusus dipakai untuk mendeteksi kapan teks yang diberikan sudah terdekripsi.

Dan itu hanya baru puncak dari gunung es. Untuk penjelasan teknis yang lebih lengkap, lihat [dokumentasi](https://docs.ciphey.online/en/latest) kita.

# ✨ Fitur-fitur

- **Lebih dari 20 jenis enkripsi didukung** seperti penyandian (binary, base64) dan enkripsi normal seperti cipher Caesar, Transposisi dan banyak lagi. **[Untuk daftar lengkap, klik disini](https://docs.ciphey.online/en/latest/ciphers.html)**
- **Ciphey mengunakan modul kecerdasan buatan dengan Pencarian Bertambah (_AuSearch_) untuk menjawab pertanyaan "enkripsi apa yang digunakan?"** Ini memunkinkan dekripsi untuk membutuhkan waktu kurang dari 3 detik. 
- **Modul pemrosesan bahasa alami yang dibangun khusus** Ciphey dapat mendeteksi ketika sesuatu adalah teks biasa dengan akurasi yang sangat tinggi dan dengan cepat.
- **Dukungan Multi Bahasa** saat ini, hanya Bahasa Jerman & Inggris (dengan varian AU, UK, CAN, USA) yang tersedia.
- **Mendukung enkripsi** yang alternatif seperti CyberChef Magic tidak memiliki. 
- **[Memakai inti C++](https://github.com/Ciphey/CipheyCore)** Sangat Cepat.

# 🔭 Ciphey vs CyberChef

## 🔁 Dikodekan Base64 42 kali

<table>
  <tr>
  <th>Name</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="Pictures_for_README/ciphey_vs_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Durasi</th>
    <td>2 detik</td>
    <td>6 detik</td>
  </tr>
    <tr>
  <th>Pemakaian</th>
    <td><ul><li>Jalankan ciphey pada file</li></ul></td>
    <td><ul><li>Setel parameter regex menjadi "{"</li><li>Anda perlu tahu berapa kali untuk mengulang</li><li>Anda harus tahu teksnya dikodekan dengan Base64 sepenuhnya</li><li>Anda perluh memuat CyberChef (sebuah aplikasi JS yang besar)</li><li>Cukup tahu tentang CyberChef untuk menggunakannya dalam hal ini</li></ul></td>
  </tr>
</table>


<sub><b>Catatan</b> Gif diatas dapat memuat pada waktu yang berbeda sehingga satu terlihat jauh lebih cepat daripada yang lain.</sub><br>
<sub><b>Sebuah catatan tentang magic,</b> fitur CyberChef's yang paling mirip Ciphey. Magic gagal secara instan pada input ini dan cara satu-satunya untuk memaska CyberChef bersaing adalah untuk mendefinisikannya secara manual.</sub>


Kami juga menguji CyberChef dan Ciphey dengan file sebesar **6gb**. Ciphey memecahkannya dalam **5 menit dan 54 detik** dan CyberChef gagal bahkan sebelum memulai.



## 📊 Ciphey vs Katana vs CyberChef Magic

| **Name**                                   | ⚡ Ciphey ⚡ | 🤡 Katana 🤡 | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ---------- | ---------- | ------------------- |
| Pemerika Bahasa yang Mahir                 | ✅         | ❌         | ✅                  |
| Mendukung Enkripsi                         | ✅         | ✅         | ❌                  |
| Rilis diberi nama sesuai tema Dystopian 🌃 | ✅         | ❌         | ❌                  |
| Mendukung Fungsi Hash                      | ✅         | ✅         | ❌                  |
| Mudah dipakai                              | ✅         | ❌         | ✅                  |
| Dapat menebak enkripsi yang dipakai        | ✅         | ❌         | ❌                  |
| Dibuat untuk peretas oleh peretas          | ✅         | ✅         | ❌                  |

# 🎬 Getting Started

If you're having trouble with installing Ciphey, [read this.](https://docs.ciphey.online/en/latest/install.html)

## ‼️ Important Links (Docs, Installation guide, Discord Support)

| Installation Guide | Documentation | Discord |
| ------------------ | ------------- | ------- |
| 📖 [Installation Guide](https://docs.ciphey.online/en/latest/install.html) | 📚 [Documentation](https://docs.ciphey.online) | 🦜 [Discord](https://discord.ciphey.online)

## 🏃‍♀️Running Ciphey
There are 3 ways to run Ciphey.
1. File Input `ciphey - encrypted.txt`
2. Unqualified input `ciphey -- "Encrypted input"`
3. Normal way `ciphey -t "Encrypted input"`

![Gif showing 3 ways to run Ciphey](Pictures_for_README/3ways.gif)

To get rid of the progress bars, probability table, and all the noise use the quiet mode.

```ciphey -t "encrypted text here" -q```

For a full list of arguments, run `ciphey --help`.

### ⚗️ Importing Ciphey
You can import Ciphey\'s main and use it in your own programs and code. `from Ciphey.__main__ import main`

# 🎪 Contributors
Ciphey was invented by [Brandon Skerritt](https://github.com/brandonskerritt) in 2008, and revived in 2019. Ciphey wouldn't be where it was today without [Cyclic3](https://github.com/Cyclic3) - president of UoL's Cyber Security Society.

Ciphey was revived & recreated by the [Cyber Security Society](https://www.cybersoc.cf/) for use in CTFs. If you're ever in Liverpool, consider giving a talk or sponsoring our events. Email us at `cybersecurity@society.liverpoolguild.org` to find out more 🤠

**Major Credit** to George H for working out how we could use proper algorithms to speed up the search process.
**Special thanks** to [varghalladesign](https://www.facebook.com/varghalladesign) for designing the logo. Check out their other design work!

## 🐕‍🦺 [Contributing](CONTRIBUTING.md)
Don't be afraid to contribute! We have many, many things you can do to help out. Each of them labelled and easily explained with examples. If you're trying to contribute but stuck, tag @brandonskerritt in the GitHub issue ✨

Alternatively, join the Discord group and send a message there (link in [contrib file](CONTRIBUTING.md)) or at the top of this README as a badge.

Please read the [contributing file](CONTRIBUTING.md) for exact details on how to contribute ✨
## 💰 Financial Contributors
The contributions will be used to fund not only the future of Ciphey and its authors, but also Cyber Security Society at the University of Liverpool.

GitHub doesn't support "sponsor this project and we'll evenly distribute the money", so pick a link and we'll sort it out on our end 🥰

## ✨ Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://skerritt.blog"><img src="https://avatars3.githubusercontent.com/u/10378052?v=4" width="100px;" alt=""/><br /><sub><b>Brandon</b></sub></a><br /><a href="#design-brandonskerritt" title="Design">🎨</a> <a href="#maintenance-brandonskerritt" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=brandonskerritt" title="Code">💻</a> <a href="#ideas-brandonskerritt" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/Cyclic3"><img src="https://avatars1.githubusercontent.com/u/15613874?v=4" width="100px;" alt=""/><br /><sub><b>cyclic3</b></sub></a><br /><a href="#design-cyclic3" title="Design">🎨</a> <a href="#maintenance-cyclic3" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=cyclic3" title="Code">💻</a> <a href="#ideas-cyclic3" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/michalani"><img src="https://avatars0.githubusercontent.com/u/27767884?v=4" width="100px;" alt=""/><br /><sub><b>michalani</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=michalani" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ashb07"><img src="https://avatars2.githubusercontent.com/u/24845568?v=4" width="100px;" alt=""/><br /><sub><b>ashb07</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=ashb07" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
