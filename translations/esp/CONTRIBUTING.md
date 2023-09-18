<p align="center">
Translations <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/CONTRIBUTING.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/CONTRIBUTING.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/CONTRIBUTING.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/CONTRIBUTING.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/CONTRIBUTING.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/CONTRIBUTING.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/CONTRIBUTING.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/CONTRIBUTING.md>🇨🇳 ZH   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/es/CONTRIBUTING.md>es ES  </a>
</p>

¡Hola!

Entonces, ¿estás interesado en contribuir a Ciphey? 🤔

¿Quizás no sabe por dónde empezar o cree que sus habilidades de codificación no son "lo suficientemente buenas"? Bueno, para esto último, ¡eso es ridículo! Estamos perfectamente de acuerdo con el "código incorrecto" e incluso así, si estás leyendo este documento, probablemente seas un gran programador. Quiero decir, los novatos no suelen aprender a contribuir a proyectos de GitHub. 😉

Aquí hay algunas maneras en que puede contribuir a Ciphey:

- Agregar un nuevo idioma 🧏
- Agregar más métodos de cifrado 📚
- Crear más documentación (¡muy importante! Estaríamos eternamente agradecidos)
- Solucionar errores enviados a través de problemas de GitHub (podemos ayudarle en esto 😊)
- Refactorizar la base del código 🥺

Si esto le suena difícil, ¡no se preocupe! Este documento le explicará exactamente cómo lograr cualquiera de estos. Además, su nombre se agregará a la lista de colaboradores de Ciphey y estaremos eternamente agradecidos. 🙏

Tenemos un pequeño chat de Discord para que hables con los desarrolladores y obtengas ayuda. Alternativamente, puedes escribir un número de GitHub para tu sugerencia. Si quieres que te agreguemos a Discord, envíanos un mensaje privado o pregúntanos de alguna manera.

[Discord Server](https://discord.gg/KfyRUWw)

# Como contribuir

¡Ciphey siempre necesita más herramientas de descifrado! Para aprender cómo integrar código en ciphey, consulte:

- <https://github.com/Ciphey/Ciphey/wiki/Adding-your-own-ciphers> para un tutorial sencillo
- <https://github.com/Ciphey/Ciphey/wiki/Extending-Ciphey> para una referencia de API

Sería bueno si escribieras algunas pruebas, simplemente copiando una función en Ciphey/tests/test_main.py y reemplazando el texto cifrado con algo codificado con tu cifrado. Si no agrega pruebas, probablemente las fusionaremos de todos modos, ¡pero será mucho más difícil para nosotros diagnosticar errores!

¡No hace falta decir que lo agregaremos a la lista de contribuyentes por su arduo trabajo!

# Agregar un nuevo idioma 🧏

El verificador de idioma predeterminado, `brandon`, funciona con varios idiomas. Ahora bien, esto puede parecer desalentador.
Pero, sinceramente, todo lo que tienes que hacer es tomar un diccionario, hacer un pequeño análisis (hemos escrito código para ayudarte con esto), agregar los diccionarios y el análisis a un repositorio. Y luego agregue la opción a `settings.yml`.

# Crear más documentación

La documentación es la parte más importante de Ciphey. Ninguna documentación es una deuda de código extrema, y ​​no queremos eso.

Créame cuando digo que si contribuye a una excelente documentación, será visto al mismo nivel que los contribuyentes de código. La documentación es absolutamente vital.

Hay muchas maneras de agregar documentación.

- Cadenas de documentos en el código
- Mejorando nuestra documentación actual (README, este archivo, nuestras páginas Ciphey Wiki)
- Traducir documentación

¡Y mucho más!

# Corregir errores

¡Visite nuestra página de problemas de GitHub para encontrar todos los errores que tiene Ciphey! Aplástalos y serás agregado a la lista de contribuyentes. ;)

# Refactorizar la base del código

No todo Ciphey sigue PEP8 y parte del código se repite.
