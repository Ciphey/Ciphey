Howdy! 

Jadi, Anda tertarik untuk berkontribusi di Ciphey? 🤔

Tapi mungkin Anda bingung harus mulai dari mana, atau Anda yakin bahwa keahlian coding Anda tidak "cukup baik". Nah, untuk yang terakhir - itu konyol! Kami baik-baik saja dengan "kode buruk", dan meskipun demikian, jika Anda membaca dokumen ini, Anda mungkin seorang programmer yang hebat. Maksud saya, pemula jarang sekali belajar berkontribusi pada proyek GitHub 😉

Berikut beberapa cara Anda dapat berkontribusi kepada Ciphey:
* Tambahkan bahasa baru 🧏
* Tambahkan lebih banyak metode enkripsi 📚
* Buat lebih banyak dokumentasi (sangat penting‼️ Kami akan berterima kasih selamanya)
* Perbaiki bug yang dikirimkan melalui GitHub Issues (kami dapat membantu Anda dalam hal ini 😊)
* Refactor basis kode 🥺

Jika ini terdengar sulit, jangan khawatir! Dokumen ini akan memandu Anda bagaimana tepatnya mencapai semua ini. Dan juga... Nama Anda akan ditambahkan ke daftar kontributor Ciphey, dan kami akan sangat berterima kasih! 🙏


Kami memiliki Discord server kecil agar Anda dapat berbicara dengan pengembang Ciphey dan mendapatkan bantuan. Atau, anda juga bisa menulis saran-saran anda di GitHub issue kita. Jika Anda ingin ditambahkan ke Discord, DM kami atau tanyakan kepada kami.

[Server Discord](https://discord.gg/KfyRUWw)
# Bagaimana cara berkontribusi?
Ciphey selalu membutuhkan lebih banyak alat dekripsi! Untuk mempelajari cara mengintegrasikan kode ke dalam ciphey, bacalah:
* https://github.com/Ciphey/Ciphey/wiki/Adding-your-own-ciphers untuk tutorial sederhana
* https://github.com/Ciphey/Ciphey/wiki/Extending-Ciphey untuk referensi API

Akan lebih bagus jika anda bisa menulis beberapa test untuknya. Ini bisa dilakukan hanya dengan menyalin fungsi di Ciphey/tests/test_main.py dan menganti ciphertest dengan sesuatu yang dikodekan dengan cipher anda. Jika anda tidak menambahkan test, ada kemungkinan besar kami akan tetap menggabungkannya, tetapi akan lebih sulit bagi kamu untuk mendiagnosis bug!

Tak perlu dikatakan bahwa kami akan menambahkan Anda ke daftar kontributor atas kerja keras Anda!

# Tambahkan bahasa baru 🧏
Pemeriksa bahasa yang kita pakai, `brandon`, berfungsi dengan banyak bahasa. Sekarang, ini mungkin terdengar menakutkan.
Tapi sejujurnya, yang harus Anda lakukan adalah mengambil kamus, melakukan sedikit analisis (kami telah menulis kode untuk membantu Anda dalam hal ini), menambahkan kamus dan analisisnya ke repo. Dan kemudian tambahkan opsi ke `settings.yml`.

# Buat lebih banyak dokumentasi
Dokumentasi adalah bagian terpenting dari Ciphey. Tidak ada dokumentasi merupakan hutang kode yang ekstrim, dan kami tidak menginginkannya. 

Dan percayalah ketika saya mengatakan, jika Anda berkontribusi dengan baik kepada dokumentasi, Anda akan berada pada level yang sama dengan kontributor kode. Dokumentasi sangatlah vital.

Ada banyak cara anda bisa menambahkan dokumentasi.
* Menambahkan Docstrings di kode
* Membaikan dokumentasi kamu saat ini (README, file ini, halaman Read The Docs kami)
* Menerjemahkan dokumentasi

dan lain-lain!

# Perbaiki Bug
Kunjungi halaman GitHub Issue kami untuk menemukan semua bug yang dimiliki Ciphey! Dan hancurkan mereka, Anda akan ditambahkan ke daftar kontributor ;)

# Refacor basis kode
Tidak semua kode Ciphey mengikuti PEP8, dan beberapa kode diulang-ulang.
