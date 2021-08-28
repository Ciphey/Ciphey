<!-- comunity -->
<!-- [markdownlint-enable](https://github.com/AABur) -->

<p align="center">
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/README.md>🇬🇧 EN   </a>
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
<a href="https://github.com/Ciphey/Ciphey/wiki">Документация</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Руководство по установке</a>
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
<br><br>
Полностью автоматизированный инструмент для дешифровки/декодирования/взлома, основанный на обработке естественного языка и искусственном интеллекте, и немного на здравом смысле.
<br><br>
</p>
<hr>

## [Руководство по установке](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python                                           | <p align="center"><a href="https://hub.docker.com/r/remnux/ciphey">🐋 Docker (Universal)                        | <p align="center"><a href="https://ports.macports.org/port/ciphey/summary">🍎 MacPorts (macOS)                    | <p align="center"><a href="https://formulae.brew.sh/formula/ciphey">🍺 Homebrew (macOS/Linux)                     |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/macports.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/homebrew.png" /></p> |
| `python3 -m pip install ciphey --upgrade`                                                                      | `docker run -it --rm remnux/ciphey`                                                                            | `sudo port install ciphey`                                                                                       | `brew install ciphey`                                                                                            |

| Linux                                                                                                                   | Mac OS                                                                                                                     | Windows                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |

<hr>

# 🤔 Что это?

Введите зашифрованный текст, получите расшифрованный текст.

> "Какой тип шифрования?"

В том-то и дело. Ты не знаешь, ты просто знаешь, что это, возможно, зашифровано. Ciphey поможет тебе разобраться.

Ciphey может справиться с большинством задач за 3 секунды и даже меньше.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

Цель Ciphey - стать инструментом для автоматизации множества расшифровок и дешифровок, таких как шифрование на нескольких базах, классические шифры, хэши и более сложные криптографии.

Если вы не знаете достаточно много о криптографии или хотите быстро проверить зашифрованный текст, прежде чем работать над ним самостоятельно, Ciphey - для вас.

**Техническая часть.** Ciphey использует специально созданный модуль искусственного интеллекта (_AuSearch_) с интерфейсом обнаружения шифров, чтобы приблизительно определить, чем что-то зашифровано. Затем используется собственный настраиваемый интерфейс обработки естественного языка, который может определить, когда полученный зашифрованный текст становится обычным.

Здесь нет нейронных сетей или раздутого ИИ. Мы используем только то, что быстро и минимально.

И это только верхушка айсберга. Полное техническое объяснение можно найти в нашей [документации](https://github.com/Ciphey/Ciphey/wiki).

# ✨ Возможности

- Поддерживается **50+ шифров и кодировок**, таких как двоичный код, код Морзе и Base64. Классические шифры, такие как шифр Цезаря, Аффинный шифр и шифр Виженера. А также современные шифры, такие как XOR с повторяющимся ключом и другие. **[Полный список можно посмотреть здесь](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Собственный искусственный интеллект с расширенным поиском (AuSearch) для ответа на вопрос "какое шифрование использовалось?"**. В результате расшифровка занимает менее 3 секунд.
- **Собственный модуль обработки естественного языка** Ciphey может определить, является ли нечто простым текстом или нет. Будь то JSON, CTF-флаг или английский язык, Ciphey может определить это за пару миллисекунд.
- **Мультиязычная поддержка** _(в настоящее время только немецкий и английский языки (с вариантами AU, UK, CAN, USA))_.
- **Поддерживает шифрование и хэширование**, которых нет у других продуктов, таких как CyberChef Magic.
- **[Ядро на C++](https://github.com/Ciphey/CipheyCore)** Работает невероятно быстро.

# 🔭 Ciphey в сравнении с CyberChef

## 🔁 Base64 закодированный 42 раза

<table>
  <tr>
  <th>Продукт</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Время</th>
    <td>2 секунды</td>
    <td>6 секунд</td>
  </tr>
    <tr>
  <th>Настройка</th>
    <td><ul><li>Запустите Ciphey с файлом</li></ul></td>
    <td><ul><li>Установить параметр регекса - "{"</li><li>Вам нужно знать, сколько раз нужно выполнить перебор.</li><li>Вы должны заранее знать, что это Base64</li><li>Вы необходимо загрузить CyberChef (это раздутое JS-приложение)</li><li>Знать достаточно о CyberChef, чтобы создать этот пайплайн</li><li>Инвертировать соответствия</li></ul></td>.
  </tr>
</table>

<sub><b>Примечание:</b> gif могут загружаться в разное время, поэтому один из них может появиться значительно быстрее другого.</sub><br>
<sub><b>Примечание о магии:</b> Сильнее всего CyberChef схож с Ciphey операцией Magic. На этих данных Magic мгновенно падает и выходит из строя. Единственный способ заставить CyberChef работать - это вручную задать параметры.</b>.


Мы также протестировали CyberChef и Ciphey с **файлом размером 6 Гб**. Ciphey взломал его за **5 минут и 54 секунды**. CyberChef потерпел крах, даже не начав работу.

## 📊 Сравнение Ciphey с Katana и CyberChef Magic

| **Продукт**                                           | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ----------------------------------------------------- | ---------- | ---------- | ------------------- |
| Расширенная проверка языка                            | ✅          | ❌          | ✅                   |
| Поддержка шифрования                                  | ✅          | ✅          | ❌                   |
| Выпуски, названные в честь антиутопий 🌃               | ✅          | ❌          | ❌                   |
| Поддержка хеширования                                 | ✅          | ✅          | ❌                   |
| Простая настройка                                     | ✅          | ❌          | ✅                   |
| Может предположить использованное средство шифрования | ✅          | ❌          | ❌                   |
| Создано хакерами для хакеров                          | ✅          | ✅          | ❌                   |

# 🎬 Начало работы

Если у вас возникли проблемы с установкой Ciphey, [прочтите это.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Важные ссылки (Документация, Руководство по установке, Поддержка в Discord)

| Руководство по установке                                                         | Документация                                            | Discord                                    | Docker Image (REMnux)                                                                               |
| -------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| 📖 [Руководство по установке](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Документация](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.ciphey.online) | 🐋 [Docker Image (REMnux)](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey) |

## 🏃‍♀️Запуск Ciphey

Есть 3 способа запустить Ciphey:

1. запуск с файлом `ciphey -f encrypted.txt`
2. запуск с неопределённым текстом `ciphey -- "Encrypted input"`
3. нормальный способ запуска `ciphey -t "Encrypted input"`

![Gif, показывающий 3 способа запуска Ciphey](https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/3ways.gif)

Чтобы избавиться от прогресс-баров, таблицы вероятностей и всего шума, используйте тихий режим.

```sh
ciphey -t "encrypted text here" -q
```

Чтобы получить полный список аргументов, запустите `ciphey --help`.

### ⚗️ Импорт Ciphey

Вы можете импортировать Ciphey и использовать его в своих собственных программах и коде.
```python
from Ciphey.__main__ import main
```

# 🎪 Создатели

**Ciphey** был придуман [Bee](https://github.com/bee-san) в 2008 году и возрожден в 2019 году. **Ciphey** не был бы там, где он сейчас, без [Cyclic3](https://github.com/Cyclic3) - президента [UoL's Cyber Security Society](https://www.cybersoc.cf/).

**Ciphey** был возрожден и воссоздан UoL's Cyber Security Society для использования в CTF. Если вы когда-нибудь будете в Ливерпуле, подумайте о том, чтобы выступить с докладом или стать спонсором наших мероприятий. Напишите нам на `cybersecurity@society.liverpoolguild.org`, чтобы узнать больше 🤠.

Огромная благодарность George H за то, что он придумал, как мы можем использовать правильные алгоритмы для ускорения процесса поиска.
Отдельное спасибо [varghalladesign](https://www.facebook.com/varghalladesign) за разработку логотипа.

## 🐕‍🦺 [Помощь проекту](https://github.com/Ciphey/Ciphey/wiki/Contributing)

Не бойтесь вносить свой вклад! У нас есть много, много вещей, которые вы можете сделать, чтобы помочь. Каждая из них описана и легко объясняется на примерах. Если вы хотите внести свой вклад, но застряли, напишите GitHub issue укажите @bee-san ✨.

Или присоединитесь к группе Discord и отправьте сообщение там [ссылка на Wiki](https://github.com/Ciphey/Ciphey/wiki/Contributing) или в верхней части этого README в виде бейджика.

Пожалуйста, прочитайте [раздел Wiki о помощи проекту](https://github.com/Ciphey/Ciphey/wiki/Contributing) для получения точной информации о том, как внести вклад ✨.

Тем самым вы добавите свое имя в README и станете частью постоянно растущего проекта!
[![starchart.cc](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)

## 💰 Финансовая помощь

Взносы будут использованы для финансирования не только будущего Ciphey и его авторов, но и UoL's Cyber Security Society.

GitHub не поддерживает функцию "спонсируй этот проект, и мы равномерно распределим деньги", поэтому воспользуйтесь ссылкой, и мы разберемся с этим на нашей стороне 🥰.

## ✨ Авторы

Спасибо этим замечательным людям ([расшифровка emoji](https://allcontributors.org/docs/en/emoji-key)):

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

Этот проект следует спецификации [all-contributors](https://github.com/all-contributors/all-contributors). Вклад любого рода приветствуется!
