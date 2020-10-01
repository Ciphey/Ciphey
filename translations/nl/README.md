<p align="center">
Vertalingen <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/README.md>🇬🇧 EN   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇭🇺 HU   </a>
 
 <br><br>
➡️ 
<a href="https://github.com/Ciphey/Ciphey/wiki">Documentatie</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Installatie Gids</a>
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
Volledig automatische decryptie/decodering/kraak tool die gebruik maakt van natuurlijke taal verwerking en artificiële intelligentie, samen met gezond verstand.
</p>
<hr>

## [Installatie Gids](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://pypi.org/project/ciphey">🐋 Docker (Universal) |
| --------------------------- | ---------------------------------|
| <p align="center"><img src="Pictures_for_README/python.png" /></p> | <p align="center"><img src="Pictures_for_README/docker.png" /></p> |
| `python3 -m pip install ciphey --upgrade`  | `docker run -it --rm remnux/ciphey` | 


| Linux       | Mac OS | Windows     |
| ----------- | ------ | ----------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) |![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |
  

<hr>

# 🤔 Wat is dit?
Geef geëncrypteerde tekst, krijg de gedecrypteerde tekst terug.

> "Welk type encryptie?"

Dat is net het punt. Dat weet je niet, je weet enkel dat het mogelijks geëncrypteerd is. Ciphey zal de rest voor jouw uitzoeken.

Ciphey kan de meeste dingen oplossen in 3 seconden of minder.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

Ciphey wil een tool zijn die veel decryptie & decodering automatiseert, zoals meerdere base coderingen, klassieke coderingen of meer geavanceerde cryptografie. 

Als u niet veel weet over cryptografie, of als u snel de geëncrypteerde tekst wilt controleren voordat u er zelf aan gaat werken, dan is Ciphey iets voor u.

**Het Technische Deel.** Ciphey maakt gebruik van een zelfgemaakte kunstmatige intelligentiemodule (_AuSearch_) met een _Cipher Detection Interface_ om te raden met wat iets is geëncrypteerd. En dan een zelfgemaakte, aanpasbare natuurlijke taalverwerking _Language Checker Interface_, dewelke kan detecteren of de gegenereerde tekst overeenkomt met gedecrypteerde tekst.

Geen neurale netwerken of opgeblazen AI hier. We gebruiken enkel wat snel en minimalistisch is.

En dat is nog maar de tip van de ijsberg. Voor de volledige technische uitleg, check onze [documentatie](https://github.com/Ciphey/Ciphey/wiki).
# ✨ Functies

- **Ondersteuning voor 30+ soorten encryptie** zoals coderingen (binary, base64) en normale encryptie zoals Caesar cipher, repeating-key XOR en meer. **[Voor de volledige lijst, klik hier](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Zelfgemaakte kunstmatige intelligentiemodule met Augmented Search (AuSearch) voor het beantwoorden van vragen als "Welke encryptiemethode werd hier gebruikt?"** Wat er voor zorgt dat decryptie minder dan 3 seconden duurt. 
- **Zelfgemaakte natuurlijke taalverwerking module** Ciphey kan detecteren wanneer iets is gedecrypteerd of niet. Ongeacht of deze tekst JSON, een CTF vlag of Engels is, Ciphey krijgt het op enkele milliseconden klaar.
- **Ondersteuning voor meerdere talen** op dit moment, wordt enkel Duits & Engels (met AU, UK, CAN, USA varianten).
- **Ondersteuning voor encryptiemethodes en hashes** dewelke alternatieven zoals CyberChef Magic niet bevatten. 
- **[C++ kern](https://github.com/Ciphey/CipheyCore)** Razendsnel.

# 🔭 Ciphey vs CyberChef

## 🔁 42 keer  Base64 Gecodeerd

<table>
  <tr>
  <th>Naam</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Tijd</th>
    <td>2 seconden</td>
    <td>6 seconden</td>
  </tr>
    <tr>
  <th>Opstelling</th>
    <td><ul><li>Voer ciphey uit op het bestand</li></ul></td>
    <td><ul><li>Zet de regex parameter op "{"</li><li>Je moet weten hoeveel recursie je nodig hebt</li><li>Je moet weten dat het heel de tijd base64 nodig heeft</li><li>Je moet CyberChef inladen (het is een overbodig grote JS app)</li><li>Genoeg van CyberChef weten om deze opstelling te kunnen bekomen</li><li>Het resultaat inverteren</li></ul></td>
  </tr>
</table>


<sub><b>Note</b> De gifs kunnen op verschillende momenten inladen, waardoor de ene significant sneller zou kunnen lijken dan de andere.</sub><br>
<sub><b>Een opmerking over Magic</b>CyberChef's meest gelijkaardige functie aan Ciphey is Magic. Magic faalt meteen op deze input en crasht. De enige manier waarop we CyberChef konden dwingen om te concurreren was om alles manueel te definiëren.</sub>


We hehben ook CyberChef en Ciphey getest met een **6gb groot bestand**. Ciphey kraakt dit in **5 minuten en 54 seconden**. CyberChef crasht voor het nog maar kon beginnen.



## 📊 Ciphey vs Katana vs CyberChef Magic

| **Naam**                                   | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ---------- | ---------- | ------------------- |
| Geavanceerde Taalcontrole                  | ✅          | ❌          | ✅                   |
| Ondersteunt Encryptie                      | ✅          | ✅          | ❌                   |
| Releases genoemd naar Dystopische thema's 🌃 | ✅          | ❌          | ❌                   |
| Ondersteunt hashes                         | ✅          | ✅          | ❌                   |
| Makkelijk te installeren                   | ✅          | ❌          | ✅                   |
| Kan raden waarmee iets is geëncrypteerd    | ✅          | ❌          | ❌                   |
| Gemaakt voor hackers door hackers          | ✅          | ✅          | ❌                   |

# 🎬 Aan de slag

Als je problemen hebt met het installeren van Ciphey, [lees dit.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Belangrijke links (Docs, Installatie Gids, Discord Support)

| Installation Gids | Documentatie | Discord | Docker Image (from REMnux)
| ------------------ | ------------- | ------- | ------- | 
| 📖 [Installatie Gids](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Documentatie](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.ciphey.online) | 🐋 [Docker Documentatie](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey)

## 🏃‍♀️ Ciphey Gebruiken
Er zijn 3 manieren om Ciphey te gebruiken.
1. Bestand invoer `ciphey -f encrypted.txt`
2. Ongekwantificeerde input `ciphey -- "Encrypted input"`
3. Normale manier`ciphey -t "Encrypted input"`

![Gif die de 3 manieren toont om Ciphey te gebruiken](Pictures_for_README/3ways.gif)

Om van de progressie bar, kansen tafel en al het andere lawaai af te geraken, gebruikt de stille modus.

```ciphey -t "encrypted text here" -q```

Voor een volledige lijst van argumenten, voer `ciphey --help` uit.

### ⚗️ Ciphey Importeren
Je kan Ciphey\'s main importeren en gebruiken in je eigen code. `from Ciphey.__main__ import main`
# 🎪 Bijdragers
Ciphey is uitgevonden door [Brandon](https://github.com/bee-san) in 2008, en nieuw leven ingeblazen in 2019. Ciphey zou niet staan waar het vandaag de dag staat zonder [Cyclic3](https://github.com/Cyclic3) - president van UoL's Cyber Security Society.

Ciphey werd nieuw leven ingeblazen & hermaakt door de [Cyber Security Society](https://www.cybersoc.cf/) voor gebruik in CTFs. Moest je ooit in Liverpool zijn, overweeg een lezing te houden of onze evenementen te sponsoren. E-mail ons op `cybersecurity@society.liverpoolguild.org` om meer te weten te komen 🤠

**Zeer Grote Dank** aan George H om uit te zoeken hoe we de juiste algoritmen kunnen gebruiken om het zoekproces te versnellen.
**Grote Dank** to [varghalladesign](https://www.facebook.com/varghalladesign) voor het ontwerpen van het logo. Bekijk hun andere ontwerpen!

## 🐕‍🦺 [Bijdragen](https://github.com/Ciphey/Ciphey/wiki/Contributing)
Wees niet bang om bij te dragen! Wij hebben veel dingen die je kan doen om te helpen. Elk waarvan een label hebben en een uitleg met voorbeelden. Moest je vast geraken, tag @bee-san of @cyclic3 in de GithHub Issue ✨
Je kunt ook lid worden van de Discord-groep en daar een bericht sturen (link in [bijdrager bestand](https://github.com/Ciphey/Ciphey/wiki/Contributing)) of bovenaan deze README als badge.

Lees het [bijdrager bestand](https://github.com/Ciphey/Ciphey/wiki/Contributing) voor exacte details over hoe u kunt bijdragen ✨

Door dit te doen, wordt uw naam toegevoegd aan de README hieronder en kunt u deel uitmaken van een steeds groter wordend project!
[![Stargazers over tijd](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)
## 💰 Financiële bijdragers
De bijdragen zullen niet alleen worden gebruikt om de toekomst van Ciphey en zijn auteurs te financieren, maar ook om Cyber Security Society aan de Universiteit van Liverpool te financieren.

GitHub ondersteunt "sponsor this project and we'll evenly distribute the money" niet, dus kies een link en we lossen het aan onze kant op 🥰

## ✨ Bijdragers

Dank aan deze geweldige mensen ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

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
    <td align="center"><a href="https://tuxthexplorer.github.io/"><img src="https://avatars1.githubusercontent.com/u/37508897?v=4" width="100px;" alt=""/><br /><sub><b>TuxTheXplorer</b></sub></a><br /><a href="#translation-TuxTheXplorer" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/Itamai"><img src="https://avatars3.githubusercontent.com/u/53093696?v=4" width="100px;" alt=""/><br /><sub><b>Itamai</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Itamai" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3AItamai" title="Bug reports">🐛</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

Dit project volgt de [all-contributors](https://github.com/all-contributors/all-contributors) specificatie. Bijdragen van welke aard dan ook zijn welkom!
