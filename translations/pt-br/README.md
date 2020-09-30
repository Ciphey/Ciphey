<p align="center">
Traduções <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/README.md>🇧🇷 PT-BR   </a>
 <br><br>
➡️ 
<a href="https://github.com/Ciphey/Ciphey/wiki">Documentação</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Guia de Instalação</a>
 ⬅️

<br>
  <img src="../../Pictures_for_README/binoculars.png" alt="Ciphey">
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
Ferramenta de decifrar/decodificar completamente automatizada usando processamento de linguagem natural e inteligência artificial, também com um pouco de senso comum.
</p>
<hr>

## [Guia de instalação](https://github.com/Ciphey/Ciphey/wiki/Installation) (Em inglês)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://pypi.org/project/ciphey">🐋 Docker (Universal) |
| --------------------------- | ---------------------------------|
| <p align="center"><img src="../../Pictures_for_README/python.png" /></p> | <p align="center"><img src="../../Pictures_for_README/docker.png" /></p> |
| `python3 -m pip install ciphey --upgrade`  | `docker run -it --rm remnux/ciphey` | 


| Linux       | Mac OS | Windows     |
| ----------- | ------ | ----------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) |![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |
  

<hr>

# 🤔 Oque é ciphey?
Entra texto criptografado e sai descriptografado.

> "Que tipo de criptografia?"

Esse é a questão. Você não sabe, você só sabe que está possivelmente criptografado. Ciphey vai descobrir para você.

Ciphey pode resolver a maioria das coisas em 3 segundos ou menos.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="../../Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

Ciphey pretende ser uma ferramenta para automatizar uma boa parte de descriptografias e decodificações como por exemplo: codificações em multiplas bases, cifras classicas, hashes ou até criptografias mais avançadas.

Se você não sabe muito sobre criptografia, ou quer verificar rapidamente o texto cifrado antes de trabalhar nele você mesmo, Ciphey é para você.

**A parte técnica** Ciphey usa um módulo customizado de inteligência artificial (_AuSearch_) com uma _Interface de detecção de cifras_ para aproximar qual criptografia é usada. E então um processamento de linguagem natural customizado _Interface de verificação de linguagem_, que consegue detectar quando um texto dado vira um texto simples.

Sem redes neurais nem uma IA pesada. Nós apenas usamos oque é rápido e mínimo.

E essa é apenas a ponta do iceberg. Para a explicação técnica completa, visite a nossa [documentação](https://github.com/Ciphey/Ciphey/wiki) (Em inglês).

# ✨ Oque ciphey oferece

- **Mais de 30 criptografias** como codificações (binário, base64) e criptografias normais como cifra de Caesar, XOR com chave repetida e mais. **[Para a lista inteira clique aqui](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Inteligência artificial customizada com Busca Aumentada (AuSearch) para responder a questão "que tipo de criptografia foi usada?"** Resultando em descriptografias que tomam menos de 3 segundos.
- **Módulo customizado de Processamento de linguagem natural** Ciphey pode determinar quando algo é texto simples ou não. Se aquele texto é JSON, uma bandeira de CTF ou inglês. Cipey consegue descobrir em milisegundos.
- **Suporte em multiplas linguagens** no momento apenas Alemão e Inglês (com variações de AU, UK, CAN, USA).
- **Suporta criptografias e hashes** Que no caso as alternativas como CyberChef Magic não suportam.
- **[Núcleo em C++](https://github.com/Ciphey/CipheyCore)** Incrivelmente rápido.

# 🔭 Ciphey contra CyberChef

## 🔁 Codficado 42 vezes com Base64

<table>
  <tr>
  <th>Nome</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="../../Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="O cara que ela fala para você não se preocupar"></td>
    <td><img src="../../Pictures_for_README/not_dying.gif" alt="Você"></td>
  </tr>
  <tr>
  <th>Tempo</th>
    <td>2 segundos</td>
    <td>6 segundos</td>
  </tr>
    <tr>
  <th>Configurando</th>
    <td><ul><li>Execute Ciphey com o arquivo.</li></ul></td>
    <td><ul><li>Defina o parâmetro de regex como "{"</li>
    <li>Você deve saber a profundidade da recursão</li>
    <li>Você deve saber que é base64 até o fim</li>
    <li>Você tem que carregar o CyberChef (é uma aplicação em JS pesada)</li>
    <li>Saber o suficiente sobre CyberChef para fazer essa sequência de instruções</li>
    <li>Inverter a combinação</li></ul></td>
  </tr>
</table>


<sub><b>Nota</b> Os gifs podem carregar em tempos diferentes, então um pode parecer muito mais rápido que outro.</sub><br>
<sub><b>Uma nota em Magic</b> A ferramenta do CyberChef mais similar a Ciphey é Magic. Magic falha num instante nessa entrada e quebra. A unica maneira que poderíamos forçar CyberChef para competir seria definindo-o manualmente.</sub>

Nós também testamos CyberChef e Ciphey com um **arquivo de 6gb**. Ciphey decifrou ele em **5 minutos e 54 segundos**. CyberChef quebrou antes de começar.



## 📊 Ciphey contra Katana contra CyberChef Magic

| **Name**                                   | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ---------- | ---------- | ------------------- |
| Verificação avançada de linguagem          | ✅          | ❌          | ✅                   |
| Suporta Criptografias                      | ✅          | ✅          | ❌                   |
| Lançamentos com nomes provindos de temas distópicos 🌃   | ✅          | ❌          | ❌                   |
| Suporta Hashes                             | ✅          | ✅          | ❌                   |
| Fácil de configurar                        | ✅          | ❌          | ✅                   |
| Pode descobrir qual criptografia é usada para algo | ✅          | ❌          | ❌                   |
| Criado por hackers para hackers             | ✅          | ✅          | ❌                   |

# 🎬 Começando

Se você estiver tendo problemas instalando Ciphey, [leia isso](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions) (em inglês).

## ‼️ Links importantes (Documentação, Guia de instalação, Suporte do Discord)

| Guia de instalação | Documentação  | Discord | Imagem Docker (de REMnux)
| ------------------ | ------------- | ------- | ------- | 
| 📖 [Guia de instalação](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Documentação](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.ciphey.online) | 🐋 [Documentação Docker](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey)

## 🌀Rodando Ciphey

Tem 3 maneiras de executar Ciphey.
1. Arquivo de entrada `ciphey -f criptografado.txt`
2. Entrada indefinida `ciphey -- "Entrada criptografada"`
3. Jeito normal `ciphey -t "Entrada criptografada"`

![Gif showing 3 ways to run Ciphey](../../Pictures_for_README/3ways.gif)

Para tirar as barras de progresso, tabela de probabilidade e todo ruído use o modo quieto.

```ciphey -t "texto criptografado" -q```

Para uma lista cheia de argumentos, use `ciphey --help`.

### ⚗️ Importando Ciphey
Você pode importar o arquivo main de Ciphey e usar nos seu próprio código. `from Ciphey.__main__ import main`

# 🎪 Contribuidores
Ciphey foi inventado por [Brandon](https://github.com/bee-san) em 2008 e revivido em 2019.
Ciphey não estária aqui hoje sem [Cyclic3](https://github.com/Cyclic3) - presidente da UoL's Cyber Security Society.

Ciphey foi revivido e recriado pela [Cyber Security Society](https://www.cybersoc.cf/) para uso em CTFs. Se a qualquer momento você estiver em Liverpool, considere dar uma palesta ou patrocinar nossos eventos. Nos mande um Email em  `cybersecurity@society.liverpoolguild.org` para saber mais 🤠

**Crédito principal** para George H por trabalhar em como que poderíamos usar algorítmos adequados para acelerar o processo de busca.

**Agradecimentos especiais** para [varghalladesign](https://www.facebook.com/varghalladesign) por fazer o design da logo. Confira o seu trabalho trabalho de desing!

## 🐕‍🦺 [Contribuindo](CONTRIBUTING.md)
Não tenha medo de contribuir! Nós temos varias coisas que você pode fazer para ajudar. Cada uma rotulada e explicada com exemplos. Se você estiver tentando contribuir mas estiver perdido, marque @bee-san ou @cyclic3 na issue do GitHub. ✨

Alternativamente, entre no grupo do Discord e mande uma mensagem lá (link no [arquivo de contribuição](CONTRIBUTING.md)) ou no topo desse README.

Por favor leia o [arquivo de contribuição](CONTRIBUTING.md) para detalhes exatos em como contribuir.✨

Contribuindo, você terá seu nome adicionado no README abaixo e será parte de um projeto que em crescimento!
[![Stargazers over time](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)

## 💰 Contribuições financeiras
As contribuições serão usadas para financiar não apenas o futuro de Ciphey e seus autores, mas também a Cyber Security Society na Universidade de Liverpool.

GitHub não suporta "patrocine esse projeto e dividiremos o dinheiro", então escolha um link e nós dividiremos entre nós. 🥰

## ✨ Contribuidores

Agradecimentos para essas pessoas maravilhosas ([guia de emojis](https://allcontributors.org/docs/en/emoji-key)):

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

Esse projeto segue a especificação [todos contribuidores](https://github.com/all-contributors/all-contributors). Contribuições de qualquer tipo são bem vindas!
