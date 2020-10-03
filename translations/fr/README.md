<p align="center">
Traductions <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/fr/README.md>🇫🇷 FR   </a>
 <br><br>
➡️ 
<a href="https://github.com/Ciphey/Ciphey/wiki">Documentation</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Guide d'installation</a>
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
Outils complètement automatisé de décryptage/décodage/craquage utilisant le traitement automatique du language naturel et de l'intelligence artificiel ainsi qu'un peu de bon sens.
</p>
<hr>

## [Guide d'installation](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://pypi.org/project/ciphey">🐋 Docker (Universel) |
| --------------------------- | ---------------------------------|
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> |
| `python3 -m pip install ciphey --upgrade`  | `docker run -it --rm remnux/ciphey` | 


| Linux       | Mac OS | Windows     |
| ----------- | ------ | ----------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) |![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |
  

<hr>

# 🤔 C'est quoi ?
Texte en entrée crypté, texte decrypté en sortie.

> "Quel type de cryptage ?"

C'est le but. Vous ne savez pas, vous savez simplement que c'est probablement crypté. Ciphey le déterminera pour vous.

Ciphey peut résoudre la plupart des tâches en moins de 3 secondes.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

Ciphey se veut un outil permettant d'automatiser un grand nombre de décryptages et de décodages tels que les codages à bases multiples, les chiffrages classiques, les hachages ou la cryptographie plus avancée. 

Si vous ne savez pas grand-chose sur la cryptographie, ou si vous voulez vérifier rapidement le texte chiffré avant de le traiter vous-même, Ciphey est fait pour vous.

**La partie technique.** Ciphey utilise un module d'intelligence artificielle personnalisé (_AuSearch_) avec une _interface de détection de chiffrement_ pour déterminer approximativement avec quoi la donnée est chiffrée. Puis une _interface de vérification du langage_, qui peut détecter quand le texte donné devient du texte en clair.


Pas de réseaux neuronaux ni d'IA ici. Nous n'utilisons que ce qui est rapide et minimal.

Et ce n'est que la partie visible de l'iceberg. Pour l'explication technique complète, consultez notre  [documentation](https://github.com/Ciphey/Ciphey/wiki).

# ✨ Fonctionnalités

- **Plus de 30 cryptages pris en charge** , tels que les codages (binaire, base64) et les cryptages normaux comme le chiffrement César, la clé de répétition XOR et plus encore. **[Pour la liste complète, cliquez ici](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Intelligence artificielle sur mesure avec recherche augmentée (AuSearch) pour répondre à la question "quel cryptage a été utilisé ?"** Résultant à un décryptage en moins de 3 secondes.
- **Module de traitement du langage naturel sur mesure** Ciphey peut déterminer si un texte est en clair ou non. Qu'il s'agisse de JSON, d'un drapeau du CTF ou de l'anglais, Ciphey peut l'obtenir en quelques millisecondes.
- **Support multilingue** pour l'instant, seul l'allemand et l'anglais (avec des variantes AU, UK, CAN, USA).
- **Supporte les cryptages et les hachages**, ce qui n'est pas le cas des alternatives telles que CyberChef Magic.
- **[Noyau C++](https://github.com/Ciphey/CipheyCore)** ultra rapide.

# 🔭 Ciphey vs CyberChef

## 🔁 Base64 Encodé 42 fois

<table>
  <tr>
  <th>Nom</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Temps</th>
    <td>2 seconds</td>
    <td>6 seconds</td>
  </tr>
    <tr>
  <th>Configuration</th>
    <td><ul><li>Lancer ciphey sur le fichier</li></ul></td>
    <td>
      <ul>
        <li>Régler le paramètre de regex sur "{"</li>
        <li>Vous devez savoir combien de fois il faut recommencer</li>
        <li>Vous devez savoir que c'est du Base64 à la fin</li>
        <li>Vous devez charger CyberChef (c'est une application JS volumineuse)</li>
        <li>En savoir assez sur CyberChef pour créer ce pipeline</li>
        <li>Inverser la correspondance</li>
      </ul>
    </td>
  </tr>
</table>


<sub><b>Note</b> Les gifs peuvent se charger à des moments différents, de sorte que l'un peut apparaître beaucoup plus rapidement qu'un autre.</sub><br>
<sub><b>Une note sur la magie </b>La fonctionnalité de CyberChef la plus similaire à celle de Ciphey est la magie. Magic échoue instantanément sur cette entrée et se bloque. La seule façon de forcer CyberChef à rivaliser est de le définir manuellement.</sub>


Nous avons également testé CyberChef et Ciphey avec un fichier de **6gb**. Ciphey l'a cracké en **5 minutes et 54 secondes**. CyberChef s'est planté avant même d'avoir commencé.



## 📊 Ciphey vs Katana vs CyberChef Magic

| **Nom**                                         | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ----------------------------------------------- | ------------- | ------------- | ---------------------- |
| Vérificateur de langue avancé                   | ✅           | ❌            | ✅                    |
| Prise en charge des cryptages                   | ✅           | ✅            | ❌                    |
| Sorties portant le nom de thèmes dystopiens 🌃 | ✅            | ❌            | ❌                    |
| Supporte les hashes                             | ✅           | ✅            | ❌                    |
| Facile à configurer                             | ✅           | ❌            | ✅                    |
| Peut deviner avec quoi quelque chose est crypté | ✅           | ❌            | ❌                    |
| Créé pour les hackers par les hackers           | ✅           | ✅            | ❌                    |

# 🎬  Pour commencer

Si vous avez des difficultés à installer Ciphey, [lisez ceci.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Liens importants (Documentations, Guide d'installation, Support Discord)

| Guide d'installation | Documentation | Discord | Image Docker (de REMnux)
| -------------------- | ------------- | ------- | -------------------------- | 
| 📖 [Guide d'installation](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Documentation](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.ciphey.online) | 🐋 [Documentation Docker](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey)

## 🏃‍♀️ Lancer Ciphey
Il y'a 3 manières de lancer Cyphey
1. Fichier en entrée `ciphey -f crypte.txt`
2. Entrée non qualifiée `ciphey -- "entrée cryptée"`
3. Méthode standard `ciphey -t "entrée cryptée"`

![Gif montrant 3 manières de lancer Cyphey](https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/3ways.gif)

Pour éliminer les barres de progression, le tableau des probabilités et tout le bruit, utilisez le mode silencieux.

```ciphey -t "text cryptée ici" -q```

Pour une liste complète des arguments, lancez `ciphey --help`.

### ⚗️ Importer Ciphey
Vous pouvez importer le main de Ciphey et l'utiliser dans vos propres programmes et codes. `from Ciphey.__main__ import main`

# 🎪 Contributeurs
Ciphey a été inventé par [Brandon](https://github.com/bee-san) en 2008, et relancé en 2019. Ciphey ne serait pas où il en est aujourd'hui sans [Cyclic3](https://github.com/Cyclic3) - president de la UoL's Cyber Security Society.

Ciphey a été relancé et recrée par la [Cyber Security Society](https://www.cybersoc.cf/) pour une utilisation lors de CTFs. Si jamais vous êtes à Liverpool, envisagez de donner une conférence ou de parrainer nos événements. Envoyez nous un email à `cybersecurity@society.liverpoolguild.org` pour en savoir plus 🤠

**Crédit majeur** à George H pour avoir trouvé comment nous pourrions utiliser des algorithmes appropriés pour accélérer le processus de recherche.
**Remerciements particuliers** à [varghalladesign](https://www.facebook.com/varghalladesign) pour avoir designé le logo. Jetez un coup d'oeil à leurs autres créations !

## 🐕‍🦺 [Contribuer](https://github.com/Ciphey/Ciphey/wiki/Contributing)
N'ayez pas peur de contribuer ! Nous avons de très nombreuses choses que vous pouvez faire pour nous aider. Chacune d'entre elles est étiquetée et facilement expliquée à l'aide d'exemples. Si vous essayez de contribuer mais que vous êtes bloqué, identifiez @bee-san ou @cyclic3 dans l'issue sur GitHub ✨

Vous pouvez également rejoindre le groupe Discord et y envoyer un message (lien dans le fichier de [contributions](https://github.com/Ciphey/Ciphey/wiki/Contributing)) ou en haut de ce README comme un badge.

Veuillez lire le [fichier de contribution] (https://github.com/Ciphey/Ciphey/wiki/Contributing) pour les détails exacts sur la façon de contribuer ✨

En faisant cela, votre nom sera ajouté au README ci-dessous et vous aurez la chance de faire partie d'un projet en constante évolution !

[![Stargazers dans le temps](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)

## 💰 Contributeurs financier
Les contributions serviront à financer non seulement l'avenir de Ciphey et de ses auteurs, mais aussi la Cyber Security Society de l'université de Liverpool.

GitHub ne soutient pas l'idée de "sponsoriser ce projet et nous distribuerons l'argent de manière équitable", alors choisissez un lien et nous nous en occuperons de notre côté 🥰

## ✨ Contributeurs

Merci à ces personnes formidables ([clé emoji](https://allcontributors.org/docs/en/emoji-key)):

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

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
