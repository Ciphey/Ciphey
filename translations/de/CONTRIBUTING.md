Hallo! 

Du hast also Interesse daran, etwas zu Ciphey beizutragen? 🤔

Vielleicht ist Dir nicht ganz klar, wo Du am besten anfangen sollst. Oder vielleicht denkst Du, Deine Programmierfähigkeiten seien "nicht gut genug". Was letzteres angeht - totaler Unsinn! Uns macht "schlechter Code" rein gar nichts aus. Ganz davon abgesehen spricht die Tatsache, dass Du dieses Dokument liest dafür, dass Du eine hervorragende Programmiererin/ein hervorragender Programmierer bist. Schließlich nehmen nur die wenigsten Anfänger\*innen an GitHub-Projekten teil. 😉

Hier sind ein paar Möglichkeiten, wie Du etwas beitragen kannst:
* Füge eine neue Sprache hinzu 🧏
* Entwickle eine neue Entschüsselungsmethode, die uns bisher noch fehlt. 📚 [siehe hier für die Liste](https://github.com/Ciphey/Ciphey/issues/63)
* Erstelle mehr Dokumentation (sehr wichtig‼️  Wir wären Dir ewig dankbar)
* Behebe Bugs, die in GitHub Issues eingereicht wurden (wir können Dich hierbei unterstützen 😊)
* Unsere Codebase refaktorisieren 🥺

Wenn das alles etwas schwer klingt, keine Sorge! Dieses Dokument begeleitet dich Schritt-für-Schritt bis zum Erfolg. Außerdem.... Dein Name wird zu Cipheys Liste der Mitwirkenden hinzugefügt! 
Zu guter Letzt sind wir Dir natürlich auch noch unheimlich dankbar! 🙏


Wir haben einen Discord-Server, in dem Du Kontakt zu den Entwicklerinnen & Entwicklern aufnehmen und Hilfe erhalten kannst. Alternativ kannst Du ein GitHub-Issue mit deinem Vorschlag eröffnen. 

[Discord-Server](https://discord.gg/KfyRUWw)
# Wie kann Ich beitragen?
Ciphey braucht immer neue Entschlüsselungsmodule! Um herauszufinden, wie Du Deinen Code in Ciphey integrieren kannst, schau hier rein:
* https://github.com/Ciphey/Ciphey/wiki/Adding-your-own-ciphers für eine einfache Anleitung.
* https://github.com/Ciphey/Ciphey/wiki/Extending-Ciphey für die API-Reference.

Es wäre toll, wenn Du ein paar Tests für Deinen Code schreiben könntest. Das ist ganz einfach: 
Kopiere Deine Funktion nach Ciphey/tests/test_main.py und ersetze den `ciphertext` mit etwas, das mit Deiner Methode verschlüsselt wurde. Wir werden wahrscheinlich auch Code ohne Tests mergen, dieser ist aber schwerer zu debuggen.

Selbstverständlich werden wir Dich in der Liste der Mitwirkenden für Deine harte Arbeit würdigen!

### Anmerkung für Deutschsprachige:
Falls Du Hilfe dabei brauchst, die noch nicht übersetzten Teile der englischen Dokumentation zu lesen - oder deine Codekommentare lieber auf Deutsch schreibst - stehe ich Dir gerne für die Übersetzung zur Seite: [@lukasgabriel auf GitHub](https://github.com/lukasgabriel) oder [@flyomotive auf Twitter](https://twitter.com/flyomotive) und im Discord.
Die deutsche Vereinbarung über den Verhaltenskodex der Mitwirkenden [findest Du hier](CODE_OF_CONDUCT.de.md).

# Eine neue Sprache hinzufügen 🧏
Die default-Spracherkennung `brandon` funktioniert mit mehreren Sprachen.
Obwohl es vielleicht etwas kompliziert klingt, ist es ganz einfach, eine Sprache hinzuzufügen:
Du brauchst nur ein Wörterbuch der Sprache, das Du mithilfe eines unserer Tools analysierst. Danach fügst Du das Wörterbuch und die Analyse unserem Repository hinzu. Zuletzt fügst Du die Sprachoption der `settings.yml` hinzu.

# Erstelle Dokumentation
Die Dokumentation ist der wichtigste Teil von Ciphey. Fehlende Dokumentation stellt eine enorme [technische Schuld](https://de.wikipedia.org/wiki/Technische_Schulden) dar - welche wir natürlich vermeiden wollen.

Eins ist sicher: Wenn Du gute Dokumentation beiträgst, wirst Du genauso geschätzt wie alle, die guten Code beitragen! Code zu dokumentieren ist absolut überlebenswichtig für jedes Projekt.

Es gibt viele Wege, zur Dokumentation beizutragen:
* Docstrings direkt im Code
* Verbesserung unserer bisherigen Dokumentation (READMEs, Contrib-Datei, unsere *Read The Docs* Seiten,...)
* Übersetzung von Dokumentation

Und viele weitere!

# Bugs beheben
Besuche unsere GitHub Issues, um zu sehen, welche Bugs momentan vorliegen. Wenn Du Bugs behebst, kommst Du selbstverständlich auf die Liste der Mitwirkenden ;-)

# Die Codebase refaktorisieren
PEP8 wird nicht von unserem gesamten Code eingehalten - und viele Teile des Codes bestehen doppelt.
