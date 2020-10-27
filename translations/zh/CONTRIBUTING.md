<p align="center">
翻译 <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/CONTRIBUTING.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/CONTRIBUTING.md>🇬🇧 EN   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/CONTRIBUTING.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/CONTRIBUTING.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/CONTRIBUTING.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/CONTRIBUTING.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/CONTRIBUTING.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/CONTRIBUTING.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/CONTRIBUTING.md>🇨🇳 ZH   </a>
</p>

你好！

您有兴趣为 Ciphey 做贡献吗？ 🤔

也许您对从哪里开始感到困惑，或者您认为自己的编码技能还不够“好”？好吧，对于后者-这太荒谬了！我们对“错误的代码”完全没问题，即使如此，如果您正在阅读本文档，您可能也是一个不错的程序员。我的意思是，新手通常不会学会为 GitHub 项目做贡献 😉

您可以通过以下方法为 Ciphey 做出贡献:

- 新增语言 🧏
- 添加更多加密方法 📚
- 创建更多文档（非常重要！我们将非常感激）
- 修复通过 GitHub 问题提交的错误（我们可以在此方面为您提供支持 😊)
- 重构代码库 🥺

如果这些听起来很难，请不要担心！本文档将引导您确切地实现这些目标。另外，您的名字也会被添加到 Ciphey 的贡献者列表中，我们将永远感谢您！ 🙏

我们有一个小的 Discord 聊天室供您与开发人员交谈并获得帮助。或者，您可以为您的建议写一个 GitHub 问题。如果您想加入 Discord，请与我们联系或以某种方式询问我们[Discord 链接](https://discord.gg/KfyRUWw)

# 如何贡献

Ciphey 始终需要更多解密工具！要了解如何将代码集成到 ciphey 中，请查看:

- <https://github.com/Ciphey/Ciphey/wiki/Adding-your-own-ciphers> 一个非常简单的教程
- <https://github.com/Ciphey/Ciphey/wiki/Extending-Ciphey> 有关 API 的参考

如果您为此编写了一些测试，那就很好了，只需在 Ciphey / tests / test_main.py 中复制一个函数，并用用密码编码的内容替换密文。如果您不添加测试，我们可能仍会合并它，但是对我们来说，诊断错误会更加困难！
不用说，我们将把您添加到您的辛勤工作的贡献者名单中！

# 新增语言 🧏

默认的语言检查器“ brandon”可使用多种语言。现在，这听起来令人生畏。
但老实说，您要做的就是拿字典，做一些分析（我们编写了代码来帮助您），将字典和分析添加到仓库中。然后将选项添加到“ settings.yml”。

# 创建更多文档

文档是 Ciphey 最重要的部分。没有文档是极端的代码负担，我们不希望如此。
当我说的时候请相信我，如果您为出色的文档做出了贡献，那么您将与代码贡献者处于同一水平。文档非常重要。

您可以通过多种方式添加文档.

- 代码中的文档字符串
- 改进我们当前的文档（自述文件，此文件，Ciphey Wiki 页面）
- 翻译文件 （这是非常重要的，越多的语言版本越好）

以及更多！

# 修正代码中的错误

访问我们的 GitHub 问题页面，查找 Ciphey 的所有错误！压扁它们，您将被添加到贡献者列表。 ;）

# 重构代码库

并非所有 Ciphey 都遵循 PEP8，并且某些代码会重复。
