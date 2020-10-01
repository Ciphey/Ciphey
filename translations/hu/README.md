<p align="center">
Fordítások <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/README.md>🇬🇧 EN   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/README.md>🇳🇱 NL   </a>

 <br><br>
➡️ 
<a href="https://github.com/Ciphey/Ciphey/wiki">Dokumentáció</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Telepítési Útmutató</a>
 ⬅️

<br>
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/binoculars.png" alt="Ciphey">
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

Teljesen automatizált dekódoló program, mely a mesterséges intelligenciát és természetes nyelvi feldolgozást használva képes különböző fajta kódolásokat visszafejteni, feltörni és dekódolni.
</p>
<hr>

## [Telepítési Útmutató](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://pypi.org/project/ciphey">🐋 Docker (Universal) |
| --------------------------- | ---------------------------------|
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> |
| `python3 -m pip install ciphey --upgrade`  | `docker run -it --rm remnux/ciphey` | 


| Linux       | Mac OS | Windows     |
| ----------- | ------ | ----------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) |![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |
  

<hr>

# 🤔 Mi is ez?
Kódolt szöveg be, dekódolt szöveg ki.

> "Milyen kódolással működik?"

A lényeg, hogy nem tudjuk előre a kódolást, csak azt, hogy a bizonyos szöveg titkosítva van. A Ciphey kitalálja nekünk a helyes kódolást.

A legtöbb kódolást Ciphey kevesebb mint 3 másodperc alatt visszafejti.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

A Ciphey projekt lényege, hogy automatizálja a monoton visszafejtési és dekódolási feladatokat, mint például a több rétegú base kódolás, klasszikus rejtjelek, hashek és bonyolultabb titkosítások megoldása.

A Ciphey-t neked találták ki ha nem vagy jártas a kriptográfia világában vagy esetleg gyorsan tesztelni szeretnél egy rejtjelezett szöveget mielőtt komolyabban nekiülnél megfejteni.  

**Mélyvíz.** Ciphey egy egyedi mesterséges intelligencia modult használ (_AuSearch_), egy úgynevezett _Cipher Detection Interface_-szel egybekötve, hogy megállapítsa egy adott szöveg hogyan van titkosítva. Ezek után egy egyedileg készített, bővíthető, természetes nyelvfeldolgozó _Language Checker Interface_-en keresztül észleli, hogy mikor kerül értelmezhetőve az adott titkosított szöveg.

Ráadásul ez még csak a jéghegy teteje. A teljes technikai tudnivalók itt érhetők el (angolul): [dokumentáció](https://github.com/Ciphey/Ciphey/wiki).

# ✨ Funkciók

- **Több mint 30 támogatott dekódolás**, mint például (bináris, base64) és rendes titkosítás, például Caesar-rejtjel, kulcs-ismétlő XOR és még több. **[A teljes listáért kattint ide](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Egyedi mesterséges intelligencia kibővített kereséssel (AuSearch), ezzel megválaszolva az "Ez milyen titkosítás?" kérdést.** Ennek eredménye a 3 másodperc alatti munkaidő. 
- **Egyedi nyelveldolgozó modul** Ciphey el tudja dönteni, hogy mi mikor van titkosítva és mikor nincs. Legyen az sima szöveg, JSON, egy CTF játék megoldása vagy angol szöveg. Ciphey néhány milliszekundom alatt megoldja.
- **Több nyelv támogatása** Jelenleg csak a német és angol nyelvek támogatottak (AU, UK, CAN, USA változatokat beleértve).
- **Titkosítás és hash támogatás** Melyeket az alternatív megoldások (például CyberChef Magic) nem támogatnak. 
- **[C++ core](https://github.com/Ciphey/CipheyCore)** Irgalmatlanul gyors.

# 🔭 Ciphey vs CyberChef

## 🔁 Base64 Dekódolás 42 alkommal egymásba ágyazva

<table>
  <tr>
  <th>Név</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Idő</th>
    <td>2 másodperc</td>
    <td>6 másodperc</td>
  </tr>
    <tr>
  <th>Futtatási feltételek</th>
    <td><ul><li>Futtasd Ciphey-t a file-on</li></ul></td>
    <td><ul><li>Állítsd be a regex paramétert "{"-re</li><li>Tudnod kell előre, hogy hányszor ismételődjon</li><li>Tudnod kell előre, hogy base64 dekódolás történik végig</li><li>Be kell tölteni a CyberChef-et (egy bonyolult JS app)</li><li>Tudnod kell eleget, hogy ezeket a CyberChefben beállítsd</li><li>Invertálnod kell a keresést</li></ul></td>
  </tr>
</table>


<sub><b>Megjegyzés</b> Lehetséges, hogy a gifek nem ugyan akkor töltenek be, ezért az egyik sokkal gyorsabbnak tűnhet.</sub><br>
<sub><b>Megjegyzés a magic-ről </b>CyberChef's leghasonlóbb funkciója Ciphey-hoz, a magic. A fentebbi teszten Magic azonnal megbukik. Egyedül úgy sikerült rávenni CyberChef-et, hogy végezzen, ha manuálisan állítottunk be mindent.</sub>

Több tesztet is végeztünk, egy **6gb-os file** segítségével. Ciphey sikeresen visszafejtette **5 perc és 54 másodperc** alatt, míg CyberChef crashelt mielőtt be tudta volna tölteni a fájlt.



## 📊 Ciphey vs Katana vs CyberChef Magic

| **Name**                                   | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ---------- | ---------- | ------------------- |
| Fejlett nyelvi elemző                      | ✅          | ❌          | ✅                   |
| Titkosítás támogatása                      | ✅          | ✅          | ❌                   |
| Releases named after Dystopian themes 🌃   | ✅          | ❌          | ❌                   |
| Hash támogatás                             | ✅          | ✅          | ❌                   |
| Egyszerű használat                         | ✅          | ❌          | ✅                   |
| Kitalálja mi mivel van titkosítva          | ✅          | ❌          | ❌                   |
| Hackereknek, hackerektől                   | ✅          | ✅          | ❌                   |

# 🎬 Kezdés

Ha problémáid akadnának a Ciphey telepítésével, [olvasd el ezt.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Fontos Linkek (Doksik, Telepítési Útmutató, Discord Támogatás)

| Telepítési Útmutató | Dokumentáció | Discord | Docker Képfájl (from REMnux)
| ------------------ | ------------- | ------- | ------- | 
| 📖 [Telepítési Útmutató](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Dokumentáció](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.ciphey.online) | 🐋 [Docker Dokumentáció](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey)

## 🏃‍♀️ Ciphey Futtatása
Ciphey három fajta módon is futtatható
1. File bemenet `ciphey -f titkosított.txt`
2. Ismeretlen bemenet `ciphey -- "Titkosított szöveg"`
3. Normális mód `ciphey -t "Titkosított szöveg"`

![Gif showing 3 ways to run Ciphey](https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/3ways.gif)

Csendes módban eltűnik a haladásjelző, valószínűség táblázat és minden más zaj.

```ciphey -t "titkosított szöveg helye" -q```

A teljes parancslistához futtasd `ciphey --help`.

### ⚗️ Ciphey importálása saját kódba
Egyszerűen importálhatod Ciphey main fűggvényét a saját kódodba. `from Ciphey.__main__ import main`

# 🎪 Közreműködők
A Ciphey-t [Brandon](https://github.com/bee-san) találta fel 2008-ban, és élesztette újjá 2019-ben. Ciphey nem tartana ma ott ahol tart [Cyclic3](https://github.com/Cyclic3) nélkül - UoL Cyber Security Society elnöke.

Ciphey-t a [Cyber Security Society](https://www.cybersoc.cf/) élesztette újra és fejleszti, elsősorban CTF játékokban való használatra. Ha Liverpoolban járnál, gondolkodj el egy előadás tartásán vagy a rendezvényeink támogatásán. Küldj emailt a `cybersecurity@society.liverpoolguild.org`-ra, hogy többet megtudj 🤠

**Fő elismerés** jár George H-nak, amiért kitalálta hogyan tudunk megefelelő algoritmusokat használni a keresés felgyorsítására.
**Különleges köszönet** jár [varghalladesign](https://www.facebook.com/varghalladesign)-nak a logó dizájnért. Nézd meg a többi dizájnt is!

## 🐕‍🦺 [Közremőködés](https://github.com/Ciphey/Ciphey/wiki/Contributing)
Ne ijedj meg a hozzájárulástól! Nagyon sok dolgunk van amiben segíthetsz. Minden felcímkézve, hogy egyszerűen megérthető legyen, példákkal. Ha lenne hozzájárulásod, de elakadtál, jelöld be @bee-san vagy @cyclic3 tagokat a GitHub issue felületen ✨

Másképpen, csatlakozz a Discord közösséghez és küldj üzenetet (link a [contrib file-ban](https://github.com/Ciphey/Ciphey/wiki/Contributing)) vagy a README tetején.

Kérlek olvasd el a [közreműködési útmutatót](https://github.com/Ciphey/Ciphey/wiki/Contributing) a pontos részlekért ✨

Ezzel, a neved bekerül a README fájlba és részese leszel egy folyamatosan növekvő projektnek!

[![Stargazers over time](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)
## 💰 Anyagi hozzájárulás
Az anyagi hozzájárulások nem csupán Ciphey jövőjét támogatják, hanem a készítőkét is, és a liverpooli Cyber Secuity Society-t.

GitHub jelenleg nem támogatja a "támogass és mi majd késöbb szétosztjuk a pénzt módszert", ezért az alábbi linkek közül válassz, a többit pedig majd mi megoldjuk. 🥰

## ✨ Közreműködők

Köszönet az alábbi csodálatos embereknek ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Cyclic3"><img src="https://avatars1.githubusercontent.com/u/15613874?v=4" width="100px;" alt=""/><br /><sub><b>cyclic3</b></sub></a><br /><a href="#design-cyclic3" title="Design">🎨</a> <a href="#maintenance-cyclic3" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=cyclic3" title="Code">💻</a> <a href="#ideas-cyclic3" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://skerritt.blog"><img src="https://avatars3.githubusercontent.com/u/10378052?v=4" width="100px;" alt=""/><br /><sub><b>Brandon</b></sub></a><br /><a href="#design-brandonskerritt" title="Design">🎨</a> <a href="#maintenance-brandonskerritt" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=brandonskerritt" title="Code">💻</a> <a href="#ideas-brandonskerritt" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/michalani"><img src="https://avatars0.githubusercontent.com/u/27767884?v=4" width="100px;" alt=""/><br /><sub><b>michalani</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=michalani" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ashb07"><img src="https://avatars2.githubusercontent.com/u/24845568?v=4" width="100px;" alt=""/><br /><sub><b>ashb07</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=ashb07" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/TheAlcanian"><img src="https://avatars3.githubusercontent.com/u/22127191?v=4" width="100px;" alt=""/><br /><sub><b>Shardion</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ATheAlcanian" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/Bryzizzle"><img src="https://avatars0.githubusercontent.com/u/57810197?v=4" width="100px;" alt=""/><br /><sub><b>Bryan</b></sub></a><br /><a href="#translation-Bryzizzle" title="Translation">🌍</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=Bryzizzle" title="Documentation">📖</a></td>
    <td align="center"><a href="https://lukasgabriel.net"><img src="https://avatars0.githubusercontent.com/u/52338810?v=4" width="100px;" alt=""/><br /><sub><b>Lukas Gabriel</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=lukasgabriel" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Alukasgabriel" title="Bug reports">🐛</a> <a href="#translation-lukasgabriel" title="Translation">🌍</a> <a href="#ideas-lukasgabriel" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/DarshanBhoi"><img src="https://avatars2.githubusercontent.com/u/70128281?v=4" width="100px;" alt=""/><br /><sub><b>Darshan</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ADarshanBhoi" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/SkeletalDemise"><img src="https://avatars1.githubusercontent.com/u/29117662?v=4" width="100px;" alt=""/><br /><sub><b>SkeletalDemise</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=SkeletalDemise" title="Code">💻</a></td>
    <td align="center"><a href="https://www.patreon.com/cclauss"><img src="https://avatars3.githubusercontent.com/u/3709715?v=4" width="100px;" alt=""/><br /><sub><b>Christian Clauss</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=cclauss" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Acclauss" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://machinexa.xss.ht"><img src="https://avatars1.githubusercontent.com/u/60662297?v=4" width="100px;" alt=""/><br /><sub><b>Machinexa2</b></sub></a><br /><a href="#content-machinexa2" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/anantverma275"><img src="https://avatars1.githubusercontent.com/u/18184503?v=4" width="100px;" alt=""/><br /><sub><b>Anant Verma</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=anantverma275" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Aanantverma275" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/XVXTOR"><img src="https://avatars1.githubusercontent.com/u/40268197?v=4" width="100px;" alt=""/><br /><sub><b>XVXTOR</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=XVXTOR" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Itamikame"><img src="https://avatars2.githubusercontent.com/u/59034423?v=4" width="100px;" alt=""/><br /><sub><b>Itamikame</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Itamikame" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/MikeMerz"><img src="https://avatars3.githubusercontent.com/u/50526795?v=4" width="100px;" alt=""/><br /><sub><b>MikeMerz</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=MikeMerz" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jacobggman"><img src="https://avatars2.githubusercontent.com/u/30216976?v=4" width="100px;" alt=""/><br /><sub><b>Jacob Galam</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=jacobggman" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

Ez a projekt megfelel az [all-contributors](https://github.com/all-contributors/all-contributors) specifikációnak. Minden nemű hozzájárulást/közreműködést szivesen látunk!
