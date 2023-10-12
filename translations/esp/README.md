<p align="center">
Translations <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/fr/README.md>🇫🇷 FR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/README.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/README.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/README.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/README.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/README.md>🇨🇳 ZH   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/es/README.md>es ES   </a>
 <br><br>
➡️
<a href="https://github.com/Ciphey/Ciphey/wiki">Documentación</a> |
<a href="https://discord.gg/zYTM3rZM4T">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Guía de instalación Guide</a>
 ⬅️

<br>
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/binoculars.png" alt="Ciphey">
</p>

<p align="center">
<img src="https://pepy.tech/badge/ciphey">
 <img src="https://pepy.tech/badge/ciphey/month">
  <a href="https://discord.gg/zYTM3rZM4T"><img alt="Discord" src="https://img.shields.io/discord/754001738184392704"></a>
<a href="https://pypi.org/project/ciphey/"><img src="https://img.shields.io/pypi/v/ciphey.svg"></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Ciphey">

<br>
Herramienta de descifrado/decodificación/craqueo totalmente automatizada que utiliza procesamiento de lenguaje natural e inteligencia artificial, junto con algo de sentido común.
</p>
<hr>

## [Guía de instalación Guide](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://hub.docker.com/r/remnux/ciphey">🐋 Docker (Universal) | <p align="center"><a href="https://ports.macports.org/port/ciphey/summary">🍎 MacPorts (macOS) | <p align="center"><a href="https://formulae.brew.sh/formula/ciphey">🍺 Homebrew (macOS/Linux) |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |--------------------------------------------------------------------------------- |
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p>    | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/macports.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/homebrew.png" /></p> |
| `python3 -m pip install ciphey --upgrade` | `docker run -it --rm remnux/ciphey` | `sudo port install ciphey` | `brew install ciphey` |

| Linux                                                                                                                   | Mac OS                                                                                                                     | Windows                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |

<hr>

# 🤔 ¿Qué es esto?

Ingrese texto cifrado y recupere el texto descifrado.

> "¿Qué tipo de cifrado?"

Ese es el punto. No lo sabes, solo sabes que posiblemente esté encriptado. Ciphey lo resolverá por ti.

Ciphey puede resolver la mayoría de las cosas en 3 segundos o menos.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

Ciphey pretende ser una herramienta para automatizar una gran cantidad de descifrados y decodificaciones, como codificaciones de base múltiple, cifrados clásicos, hashes o criptografía más avanzada.

Si no sabe mucho sobre criptografía o desea comprobar rápidamente el texto cifrado antes de trabajar en él usted mismo, Ciphey es para usted.

**La parte técnica.** Ciphey utiliza un módulo de inteligencia artificial personalizado (_AuSearch_) con un _Interfaz de detección de cifrado_ para aproximarse con qué se cifra algo. Y luego, un procesamiento de lenguaje natural personalizado y personalizable _Interfaz de verificación de idioma_, que puede detectar cuándo el texto dado se convierte en texto sin formato.

Aquí no hay redes neuronales ni IA inflada. Sólo utilizamos lo que es rápido y mínimo.

Y eso es sólo la punta del iceberg. Para obtener la explicación técnica completa, consulte nuestra [documentación](https://github.com/Ciphey/Ciphey/wiki).

# ✨ Características

- **Más de 50 cifrados/codificaciones compatibles** como binario, código Morse y Base64. Cifrados clásicos como el cifrado César, el cifrado Affine y el cifrado Vigenere. Junto con cifrado moderno como XOR de clave repetida y más. **[Para el listado entero, hacer clic aquí](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Inteligencia artificial personalizada con búsqueda aumentada (AuSearch) por responder a la pregunta "¿qué cifrado se utilizó?"** Lo que da como resultado que el descifrado tarde menos de 3 segundos.
- **Módulo de procesamiento de lenguaje natural personalizado** Ciphey puede determinar si algo es texto sin formato o no. Ya sea que ese texto sin formato sea JSON, una bandera CTF o inglés, Ciphey puede obtenerlo en un par de milisegundos.
- **Soporte en varios idiomas** Actualmente sólo alemán e inglés.(con variantes de AU, UK, CAN, USA).
- **Admite cifrados y hashes** Cosa que no hacen las alternativas como CyberChef Magic.
- **[C++ core](https://github.com/Ciphey/CipheyCore)** Increíblemente rápida.

# 🔭 Ciphey vs CyberChef

## 🔁 Base64 codificado 42 veces

<table>
  <tr>
  <th>Nombre</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Tiempo</th>
    <td>2 segundos</td>
    <td>6 segundos</td>
  </tr>
    <tr>
  <th>Configuración</th>
    <td><ul><li>Ejecute ciphey en el archivo</li></ul></td>
    <td><ul><li>Establezca el parámetro de regex expresión en "{"</li><li>Necesitas saber cuántas veces recurrir</li><li>Necesitas saber que es Base64 hasta el final</li><li>Necesitas cargar CyberChef (es una aplicación JS inflada)</li><li>Saber lo suficiente sobre CyberChef para crear este canal</li><li>invertir el partido</li></ul></td>
  </tr>
</table>

<sub><b>Nota</b> Los gifs pueden cargarse en diferentes momentos, por lo que uno puede aparecer significativamente más rápido que otro.</sub><br>
<sub><b>Una nota sobre la magia</b>La característica más similar de CyberChef a Ciphey es Magic. Magic falla instantáneamente en esta entrada y se bloquea. La única manera de obligar a CyberChef a competir era definirlo manualmente.</sub>

También probamos CyberChef y Ciphey con un **archivo de 6 gb**.Ciphey lo descifró en **5 minutos y 54 segundos**. CyberChef colapsó incluso antes de comenzar.

## 📊 Ciphey contra Katana contra CyberChef Magic

| **Nombre**                                   | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ------------ | ------------ | --------------------- |
| Comprobador de idioma avanzado             | ✅           | ❌           | ✅                    |
| Admite cifrados                            | ✅           | ✅           | ❌                    |
|Lanzamientos que llevan nombres de temas distópicos 🌃   | ✅           | ❌           | ❌                    |
| Soporta hashes                            | ✅           | ✅           | ❌                    |
| Fácil de configurar                            | ✅           | ❌           | ✅                    |
| Puede adivinar con qué está cifrado algo | ✅           | ❌           | ❌                    |
| Creado para hackers por hackers             | ✅           | ✅           | ❌                    |

# 🎬 Empezando

si tienes problemas con la instalación de Ciphey, [Lee esto.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Enlaces importantes (Documentos, guía de instalación, soporte de Discord)

| Guía de instalación                                                       | Documentación                                             | Discord                                     | Docker Image (from REMnux)                                                                          |
| --------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 📖 [Guía de instalación](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Documentación](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.gg/zYTM3rZM4T) | 🐋 [Docker Documentación](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey) |

## 🏃‍♀️Ejecutando ciphey

Hay 3 formas de ejecutar Ciphey.

1. Entrada de archivo `ciphey -f encrypted.txt`
2. Entrada no calificada `ciphey -- "Encrypted input"`
3. manera normal `ciphey -t "Encrypted input"`

![Gif que muestra 3 formas de ejecutar Ciphey](https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/3ways.gif)

Para deshacerse de las barras de progreso, la tabla de probabilidad y todo el ruido, utilice el modo silencioso.

`ciphey -t "encrypted text here" -q`

Para obtener una lista completa de argumentos, ejecute `ciphey --help`.

### ⚗️ Importando Ciphey

Puede importar el archivo principal de Ciphey y usarlo en sus propios programas y código. `from Ciphey.__main__ import main`

# 🎪 Colaboradores

Ciphey fue inventado por [Bee](https://github.com/bee-san) en 2008 y revivido en 2019. Ciphey no estaría donde está hoy sin [Cyclic3](https://github.com/Cyclic3) - Presidente de la Sociedad de Seguridad Cibernética de la UoL.

Ciphey fue revivido y recreado por el [Sociedad de seguridad cibernética](https://www.cybersoc.cf/) para uso en CTF. Si alguna vez estás en Liverpool, considera dar una charla o patrocinar nuestros eventos. Envíanos un email a `cybersecurity@society.liverpoolguild.org` para descubrir mas 🤠

**Gran crédito** para George H por descubrir cómo podríamos utilizar algoritmos adecuados para acelerar el proceso de búsqueda.
**Agradecimiento especial** a [varghalladesign](https://www.facebook.com/varghalladesign) por diseñar el logotipo. ¡Mira sus otros trabajos de diseño!

## 🐕‍🦺 [Contribuyendo](https://github.com/Ciphey/Ciphey/wiki/Contributing)

¡No tengas miedo de contribuir! Tenemos muchas, muchas cosas que puedes hacer para ayudar. Cada uno de ellos etiquetado y explicado fácilmente con ejemplos. Si estás intentando contribuir pero te quedas atascado, etiqueta a @bee-san.✨

Alternativamente, únase al grupo de Discord y envíe un mensaje allí (enlace en [archivo contribución](https://github.com/Ciphey/Ciphey/wiki/Contributing)) o en la parte superior de este README como insignia.

Por favor lea el [archivo colaborador](https://github.com/Ciphey/Ciphey/wiki/Contributing) para obtener detalles exactos sobre cómo contribuir ✨

Al hacerlo, agregarás tu nombre al archivo README a continuación y podrás ser parte de un proyecto en constante crecimiento.
[![Observadores de estrellas a lo largo del tiempo](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)

## 💰 Contribuyentes financieros

Las contribuciones se utilizarán para financiar no sólo el futuro de Ciphey y sus autores, sino también la Sociedad de Seguridad Cibernética de la Universidad de Liverpool.

GitHub no admite "patrocinar este proyecto y distribuiremos el dinero de manera equitativa", así que elige un enlace y lo solucionaremos por nuestra parte 🥰

## ✨ Colaboradores

Gracias a estos maravillosos personas ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

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

Este proyecto sigue la especificación [todos los contribuyentes] (https://github.com/all-contributors/all-contributors). ¡Bienvenidos aportes de cualquier tipo!
