<p align="center">
Übersetzungen <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/README.md>🇬🇧 EN   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/README.md>🇳🇱 NL   </a>

 <br><br>
➡️ 
<a href="https://github.com/Ciphey/Ciphey/wiki">Dokumentation</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Installationshilfe</a>
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
Vollautomatisiertes Entschlüsselungs-Tool, gestützt durch algorithmische Sprachverarbeitung & künstliche Intelligenz.
</p>
<hr>

## [Installationshilfe](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://pypi.org/project/ciphey">🐋 Docker (Universell) |
| --------------------------- | ---------------------------------|
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> |
| `python3 -m pip install ciphey --upgrade`  | `docker run -it --rm remnux/ciphey` | 


| Linux       | Mac OS | Windows     |
| ----------- | ------ | ----------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) |![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |
  

<hr>

# 🤔 Was ist Ciphey?
Ciphey ist ein vollautomatisches Entschlüsselungs-Tool. Verschlüsselter Text wird eingegeben, entschlüsselter Text kommt zurück.
> "Welche Arten von Verschlüsselung?"

Das ist die Frage. Auch wenn die Art der Verschlüsselung unbekannt ist (und lediglich die Vermutung besteht, dass es sich um verschlüsselten Text handelt), wird Ciphey einen Lösungsweg suchen.

Ciphey hat in den meisten Fällen nach circa 3 Sekunden eine Lösung parat.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

**Der technische Teil.** In Ciphey kommt ein maßgeschneidertes KI-Modul (_AuSearch_) mit Verschlüsselungserkennung (_Cipher Detection Interface_) zum Einsatz, das abschätzen kann, mit welcher Methode etwas verschlüsselt wurde. Daraufhin prüft ein dediziertes Spracherkennungs-Interface (_Language Checker Interface_), ob es sich bei dem nun entschlüsselten Text um Klartext handelt.

Und das ist erst die Spitze des Eisbergs! Eine vollständige technische Erklärung ist in der [Dokumentation](https://docs.ciphey.online/en/latest) zu finden.

# ✨ Funktionen

- **Über 20 unterstützte Verschlüsselungsarten**, zum Beispiel Kodierungen (binär, base64) und traditionelle Verschlüsselungen wie die Caesar-Verschlüsselung, Transposition und weitere. **[Vollständige Liste](https://docs.ciphey.online/en/latest/ciphers.html)**
- **Maßgeschneidertes KI-Modul mit _Augmented Search (AuSearch)_, das erkennen kann, mit welcher Methode etwas verschlüsselt wurde.** Das Ergebnis sind Laufzeiten von unter 3 Sekunden.
- **Eigens entwickeltes Spracherkennungs-Modul** Ciphey kann erkennen, ob es sich bei etwas um Klartext handelt, oder nicht. Hierbei ist es nicht nur unglaublich genau, sondern auch unglaublich schnell.
- **Mehrere unterstützte Sprachen** Momentan nur Deutsch & Englisch.
- **Unterstützt Verschlüsselungen** Im Vergleich zu Alternativen wie CyberChef Magic, die dies nicht leisten können.
- **[C++ core](https://github.com/Ciphey/CipheyCore)** Rasend schnell.

# 🔭 Ciphey vs CyberChef

## 🔁 Base64 42-fach kodiert

<table>
  <tr>
  <th>Name</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="Der Typ, bei dem sie meint, du sollst dir keine Sorgen machen."></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="Du"></td>
  </tr>
  <tr>
  <th>Zeit</th>
    <td>2 Sekunden</td>
    <td>6 Sekunden</td>
  </tr>
    <tr>
  <th>Setup</th>
    <td><ul><li>Ciphey mit der Datei ausführen</li></ul></td>
    <td><ul><li>Regex-Parameter auf "{" setzen</li><li>Die Rekursionstiefe muss bekannt sein</li><li>Vor der Ausführung muss bekannt sein, dass es sich von Anfang bis Ende um base64 handelt</li><li>CyberChef (eine aufgeblähte JavaScript-App) muss geladen werden</li><li>Genug Vorwissen über CyberChef, um diese Pipeline überhaupt aufstellen zu können</li><li>Das gefundene Korrelat umkehren</li></ul></td>
  </tr>
</table>


<sub><b>Hinweis</b> Die GIFs laden asynchron, weshalb es sein kann, dass sie nach und nach erscheinen.</sub><br>
<sub><b>Eine Bemerkung zu Magic </b>Die Magic-Funktion von CyberChef kommt Ciphey am nächsten. Magic schlägt bei dieser Eingabe sofort fehl und stürzt ab. Die einzige Möglichkeit, CyberChef (für eine Gegenüberstellung mit Ciphey) mit diesem Input zum Laufen zu bekommen war durch eine manuelle Definition durch uns.</sub>


Außerdem haben wir Ciphey und CyberChef mit einer **6GB Eingabedatei** gegeneinander antreten lassen. Ciphey hatte nach **5 Minuten und 54 Sekunden** ein Lösung. CyberChef ist abgestürzt, bevor die Entschlüsselung überhaupt begonnen hatte.



## 📊 Ciphey vs Katana vs CyberChef Magic

| **Name**                                   | ⚡ Ciphey ⚡ | 🤡 Katana 🤡 | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ---------- | ---------- | ------------------- |
| Fortschrittliche Spracherkennung           | ✅          | ❌          | ✅                   |
| Unterstützt Verschlüsselungen              | ✅          | ✅          | ❌                   |
| Releases benannt nach dystopischen Motiven 🌃   | ✅          | ❌          | ❌              |
| Unterstützt Hashes                         | ✅          | ✅          | ❌                   |
| Einfache, unkomplizierte Einrichtung       | ✅          | ❌          | ✅                   |
| Kann abschätzen, welche Verschlüsselung verwendet wurde | ✅          | ❌          | ❌      |
| Von Hackern, für Hacker                    | ✅          | ✅          | ❌                   |

# 🎬 Erste Schritte

Bei Problemen bei der Installation von Ciphey, [hier weiterlesen.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Wichtige Links (Docs, Installationshilfe, Discord Support)

| Installationshilfe | Dokumentation | Discord | Docker Image (von REMnux)
| ------------------ | ------------- | ------- | ------- | 
| 📖 [Installationshilfe](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Dokumentation](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.ciphey.online) | 🐋 [Docker Dokumentation](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey)

## 🏃‍♀️Ciphey ausführen
Es gibt 3 Möglichkeiten, Ciphey auszuführen:
1. Datei als Input `ciphey - verschluesselt.txt`
2. Unqualifizierter Input `ciphey -- "Verschlüsselter Input"`
3. Standard `ciphey -t "Verschlüsselter Input"`

![GIF zeigt drei Möglichkeiten, Ciphey auszuführen.](https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/3ways.gif)

Um die Fortschrittsanzeige, Wahrscheinlichkeitstabelle und andere Anzeigen loszuwerden, kann Ciphey im *Quiet Mode* ausgeführt werden:

```ciphey -t "Verschlüsselter Text" -q```

Fur eine komplette Liste der Argumente: `ciphey --help`.

### ⚗️ Ciphey importieren
Wer Ciphey als Teil eines eigenen Projekts verwenden will, kann es mit `from Ciphey.__main__ import main` importieren.

# 🎪 Contributors
Ciphey wurde 2008 von [Brandon Skerritt](https://github.com/brandonskerritt) erfunden und 2019 wiederbelebt. Ciphey wäre nicht dort, wo es heute ist, ohne die Hilfe von [Cyclic3](https://github.com/Cyclic3) - Präsident der *Cyber Security Society* der *University of Liverpool*.

Ciphey wurde durch die [Cyber Security Society](https://www.cybersoc.cf/) für die Verwendung in CTFs (eine Art Hacker-Wettbewerb) aufgelegt. Wenn Du jemals in Liverpool bist, würden wir uns freuen, wenn Du einen Vortrag halten oder unsere Veranstaltungen sponsern würdest. Kontaktiere uns per E-Mail unter `cybersecurity@society.liverpoolguild.org` um mehr zu erfahren. 🤠

**Einen besonderen Dienst** leistete uns George H, als er uns geholfen hat, den Suchprozess durch Algorithmen zu beschleunigen.
**Besonderer Dank** an [varghalladesign](https://www.facebook.com/varghalladesign) für die Gestaltung unseres Logos. Schau mal in das Portfolio!

## 🐕‍🦺 [Mitwirken](CONTRIBUTING.md)
Du möchtest am Projekt teilhaben - keine Angst! Wir haben sehr viele Dinge, die du tun kannst, um uns zu helfen. Jedes Issue ist gelabelt und mit Beispielen unterlegt. Falls Du feststeckst, tagge @brandonskerritt im GitHub-Issue. ✨

Alternativ kannst du unserem Discord-Server beitreten und uns dort direkt erreichen. Den Link findest du in der [Contrib-Datei](CONTRIBUTING.md) und als Badge am Anfang dieser README.

Details zur Teilnahme findest du in der [Contrib-Datei](CONTRIBUTING.md) ✨
## 💰 Finanzielle Spender
Finanzielle Beiträge werden für die zukünftige Entwicklung von Ciphey und dessen Autorinnen und Autoren verwendet. Außerdem kommen finanzielle Zuwendungen der Cyber Security Society an der University of Liverpool zugute.

Da GitHub keine gleichmäßiger Verteilung der Sponsorenbeiträge unterstützt, kannst Du dir einfach einen Link aussuchen - wir regeln den Rest dann unter uns. 🥰

## ✨ Mitwirkende

Ein Dankeschön an die folgenden großartigen Helfer: ([Legende](https://allcontributors.org/docs/en/emoji-key))

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
    <td align="center"><a href="https://lukasgabriel.net"><img src="https://avatars0.githubusercontent.com/u/52338810?v=4" width="100px;" alt=""/><br /><sub><b>Lukas Gabriel</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=lukasgabriel" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Alukasgabriel" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/DarshanBhoi"><img src="https://avatars2.githubusercontent.com/u/70128281?v=4" width="100px;" alt=""/><br /><sub><b>Darshan</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ADarshanBhoi" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/SkeletalDemise"><img src="https://avatars1.githubusercontent.com/u/29117662?v=4" width="100px;" alt=""/><br /><sub><b>SkeletalDemise</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=SkeletalDemise" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

Dieses Projekt folgt der [All-Contributors](https://github.com/all-contributors/all-contributors) Spezifikation. Jede Art von Beitrag ist herzlich willkommen!
