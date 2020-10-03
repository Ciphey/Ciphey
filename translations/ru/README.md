<p align="center">
Translations <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇭🇺 HU   </a>
 <br><br>
➡️ 
<a href="https://github.com/Ciphey/Ciphey/wiki">Документация</a> |
<a href="https://discord.ciphey.online">Раздор</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Руководство по установке</a>
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
Полностью автоматизированная дешифровка/декодирование/взлом с использованием естественного языка обработки и искусственного интеллекта, наряду с некоторым здравым смыслом.
</p>
<hr>

## [Installation Guide](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://pypi.org/project/ciphey">🐋 Docker (Universal) |
| --------------------------- | ---------------------------------|
| <p align="center"><img src="Pictures_for_README/python.png" /></p> | <p align="center"><img src="Pictures_for_README/docker.png" /></p> |
| `python3 -m pip install ciphey --upgrade`  | `docker run -it --rm remnux/ciphey` | 


| Linux       | Mac OS | Windows     |
| ----------- | ------ | ----------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) |![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |
  

<hr>

# 🤔 Что это?
Введите зашифрованный текст, получите расшифрованный текст обратно.

> "Какой тип шифрования?"

В том-то и дело. Ты не знаешь, ты просто знаешь, что это возможно зашифровано. Ciphey поможет тебе разобраться.

Ciphey может решить большинство задач за 3 секунды или меньше.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

Ciphey стремится быть инструментом для автоматизации множества расшифровок и декодировок, таких как несколько базовых кодировок, классические шифры, хэши или более продвинутая криптография. 

Если вы мало что знаете о криптографии, или хотите быстро проверить шифрованный текст перед тем, как работать над ним самостоятельно, Ciphey для вас.

**Техническая часть.** Ciphey использует пользовательский модуль искусственного интеллекта (_AuSearch_) с интерфейсом обнаружения шифров для приближения к тому, чем что-то зашифровано.  А затем настраиваемый, настраиваемый интерфейс проверки естественного языка, который может определить, когда заданный текст становится простым текстом.
Здесь нет нейронных сетей или раздутого ИИ. Мы используем только то, что быстро и минимально.

И это только верхушка айсберга. Для полного технического объяснения, посмотрите на наши [документация](https://github.com/Ciphey/Ciphey/wiki).

# ✨ Особенности

- Поддерживаются **30+ шифрования**, такие как кодировка (двоичная, base64) и обычные шифрования, например, шифр Цезаря, повторяющийся XOR и другие. **[Полный список можно посмотреть здесь](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Привычный искусственный интеллект с расширенным поиском (AuSearch) для ответа на вопрос "Какое шифрование использовалось?" ** В результате расшифровка занимает менее 3 секунд. 
- **Привычный встроенный модуль обработки естественного языка** Шифрование может определить, является ли что-то простым текстом или нет. Является ли этот чистый текст JSON, CTF-флагом или английским Ciphey может получить его за пару миллисекунд.
- **Мульти-языковая поддержка** в настоящее время, только немецкий и английский (с вариантами AU, UK, CAN, USA).
- **Помогает шифрования и хэши** Которые альтернативы, такие как CyberChef Magic не делают. 
- **[C++ core](https://github.com/Ciphey/CipheyCore)** Молниеносно быстро.

# 🔭 Ciphey в отличие от CyberChef

## 🔁 Base64 Кодируется 42 раза

<table>
  <tr>
  <th>Имя</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Тайм</th>
    <td>2 seconds</td>
    <td>6 seconds</td>
  </tr>
    <tr>
  <th>Настройка</th>
    <td><ul><li>Запустите Ciphey в файле</li></ul></td>
    <td><ul><li>Установите параметр регекса на "{"</li><li>Вы должны знать, сколько раз повторить</li><li>Вы должны знать, что это Base64 всю дорогу вниз</li><li>Вы необходимо загрузить CyberChef (это раздутое JS-приложение)</li><li>Знай достаточно о CyberChef, чтобы создать этот конвейер</li><li>Введите соответствие</li></ul></td>.
  </tr>
</table>


<sub><b>Заметка</b> gifs могут загружаться в разное время, поэтому один из них может появиться значительно быстрее другого.</sub><br>
<sub><b>Заметка о магии </b>CyberChef наиболее похожа на Ciphey - это Magic. Магия на этом входе мгновенно отказывает и падает. Единственный способ заставить CyberChef участвовать в соревнованиях - это вручную определить его.</b>.


Мы также протестировали CyberChef и Ciphey с файлом **6gb файл**. Ciphey взломал его за **5 минут и 54 секунды**. CyberChef разбился еще до того, как он запустился.



## 📊 Ciphey в отличие от Katana в отличие от CyberChef Magic

| **Имя**                                    | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ---------- | ---------- | ------------------- |
| Расширенный Проверка языка                 | ✅          | ❌          | ✅                   |
| Поддерживает шифрован                      | ✅          | ✅          | ❌                   |
| Выпуски, названные в честь антиутопических тем 🌃    | ✅          | ❌          | ❌                   |
| Поддерживает хэш                           | ✅          | ✅          | ❌                   |
| Простая настройка                          | ✅          | ❌          | ✅                   |
| Могу догадаться, чем что-то зашифровано    | ✅          | ❌          | ❌                   |
| Создано для хакеров хакерами             | ✅          | ✅          | ❌                   |

# 🎬 Начало работы

Если у тебя проблемы с установкой Ciphey, [Прочти это.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Важные ссылки (Документы, руководство по установке, Раздор Поддержка)

| Руководство по установке | Документация | Раздор | Докер изображение (от REMnux)
| ------------------ | ------------- | ------- | ------- | 
| 📖 [Руководство по установке](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Документация](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Раздор](https://discord.ciphey.online) | 🐋 [Докер изображение](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey)

## 🏃‍♀️Работающий Ciphey
Есть 3 способа запустить Ciphey.
1. Ввод файла `ciphey -f encrypted.txt`
2. Неквалифицированный ввод `ciphey -- "Encrypted input"`
3. Нормальный способ `ciphey -t "Encrypted input"`

![Gif showing 3 ways to run Ciphey](Pictures_for_README/3ways.gif)

Чтобы избавиться от индикаторов прогресса, таблицы вероятностей и всего шума, используйте тихий режим.

```ciphey -t "encrypted text here" -q```

Чтобы получить полный список аргументов, запустите `ciphey --help`.

### ⚗️ Импортирование Ciphey
Вы можете импортировать главный Ciphey\s и использовать его в своих собственных программах и коде. `from Ciphey.__main__ import main`

# 🎪 Авторы
Ciphey был придуман через [Brandon](https://github.com/bee-san) в 2008 году и возродился в 2019 году. Ciphey не был бы там, где он был сегодня без [Cyclic3](https://github.com/Cyclic3) - президент общества кибербезопасности Ливерпульского университета.

Шифры были возрождены и воссозданы [Общество кибербезопасности](https://www.cybersoc.cf/) для использования в КТФ. Если вы когда-нибудь будете в Ливерпуле, подумайте о том, чтобы выступить с докладом или спонсировать наши мероприятия. Напишите нам по адресу `cybersecurity@society.liverpoolguild.org` чтобы узнать. 🤠

**Мажорный кредит** Джорджу Х за то, что он придумал, как мы можем использовать правильные алгоритмы, чтобы ускорить процесс поиска.
**особая благодарность** [varghalladesign](https://www.facebook.com/varghalladesign) за разработку логотипа. Посмотрите на их другие работы по дизайну!

## 🐕‍🦺 [Вклад](https://github.com/Ciphey/Ciphey/wiki/Contributing)
Не бойтесь внести свой вклад! У нас есть много, много вещей, которые вы можете сделать, чтобы помочь. Каждое из них обозначено и легко объяснено примерами. Если ты пытаешься внести свой вклад, но застрял, свяжись с @bee-san или @cyclic3 в выпуске GitHub  ✨

Или присоединитесь к группе Разногласия и отправьте туда сообщение (соединяться [contrib file](https://github.com/Ciphey/Ciphey/wiki/Contributing)) или в верхней части этого значка.

Пожалуйста, ознакомьтесь с [входящий файл].(https://github.com/Ciphey/Ciphey/wiki/Contributing) для получения точной информации о том, как внести свой вклад ✨

Сделав это, вы получите ваше имя, добавленное в README ниже, и получите возможность быть отдельно от постоянно растущего проекта!
[![звёздолеты со временем](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)
## 💰 Финансовые доноры
Взносы будут использованы не только для финансирования будущего Ciphey и его авторов, но и Общества кибербезопасности Ливерпульского университета.

GitHub не поддерживает "спонсорство этого проекта, и мы будем равномерно распределять деньги", так что выбери ссылку, и мы разберемся с этим с нашей стороны. 🥰

## ✨ Авторы

Спасибо этим замечательным людям ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

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

Этот проект следует за [all-contributors](https://github.com/all-contributors/all-contributors) спецификация. Вклад любого рода приветствуется!
