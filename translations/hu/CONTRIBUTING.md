Mizu! 

Szóval érdekel a Ciphey-hoz történő közreműködés? 🤔

De lehet, hogy zavarban vagy, hogy hol kezdd, vagy úgy gondolod, hogy a kódolási képességeid nem "elég jók". Nos, ez utóbbi - nevetséges! Teljesen rendben vagyunk a "rossz kóddal", és amúgy is, ha elolvastad ezt a dokumentumot, valószínűleg remek programozó vagy. Úgy értem, az újoncok nem gyakran járulnak hozzá GitHub projektekhez 😉

Íme néhány módszer, amellyel hozzájárulhatsz a Ciphey-hoz:
* Fordítsd le egy új nyelvre 🧏
* Adj hozzá több titkosítási formát 📚
* Készíts további dokumentumokat (nagyon fontos‼️ Örökké hálásak lennénk)
* Javítsd ki a GitHub Issues-on szereplő bugokat (ebben segítünk 😊)
* Alakítsd át a kódbázist 🥺

Ha ezek keményen hangzanak, ne aggódj! Ez a dokumentum pontosan bemutatja, hogyan lehet elérni ezeket. És még többet .... A neved bekerül a Ciphey közreműködői listájába, és örökké hálásak leszünk! 🙏


Van egy kis Discord szerverünk, ahol beszélgethetsz a fejlesztőkkel, és segítséget kaphatsz. Alternatív megoldásként írj egy GitHub-Issue-t a javaslatodról. Ha csatlakozni akarsz a Discordhoz:

[Discord Server](https://discord.gg/KfyRUWw)
# Hogy lehet hozzájárulni
A Ciphey-nak mindig több dekódoló eszközre van szüksége! Ha meg szeretnéd tudni, hogyan integrálhatsz egy kódot a titkosításba, nézdd meg ezeket:
* https://github.com/Ciphey/Ciphey/wiki/Adding-your-own-ciphers Egyszerű példa
* https://github.com/Ciphey/Ciphey/wiki/Extending-Ciphey API referencia

Jó lenne, ha néhány tesztet írnál rá, egyszerűen másolj át egy függvényt a Ciphey / tests / test_main.py fájlba, és cseréld le a rejtjelszöveget a titkosításával kódolt valamire. Ha nem adsz hozzá teszteket, valószínűleg továbbra is egyesítjük a kódot, de sokkal nehezebb lesz diagnosztizálnunk a hibákat!

Magától értetődik, hogy felveszünk téged a közreműködők listájába kemény munkádért!

# Adj hozzá egy új nyelvet 🧏
Az alapértelmezett nyelvellenőrző, `brandon`, több nyelvvel is működik. Ez ijesztően hangozhat.
De őszintén szólva mindössze annyit kell tenned, hogy veszel egy szótárat, elvégzel egy kis elemzést (ehhez van segítő kódunk), majd hozzáadod a szótárat és az elemzéseket egy repóhoz. Ezután hozzáadod a nyelvet a `settings.yml` fájlhoz.

# Készíts további dokumentációt
A dokumentáció a Ciphey legfontosabb része. Minél több dokumentáció, annál jobb.

És bízz bennem, amikor azt mondom, ha hozzájárulsz a nagyszerű dokumentációhoz, akkor ugyanazon a szinten leszel látható, mint a kód-közreműködők. A dokumentáció elengedhetetlen.

Nagyon sokféleképpen járulhatsz hozzá a dokumentációhoz.
* Doc stringek beillesztése a kódba
* A jelenlegi dokumentáció javítása (README, ez a fájl, a Read The Docs oldalunk)
* Dokumentáció fordítása

És még sok más!

# Javíts bugokat
Látogass el a GitHub-Issues oldalunkra, ahol megtalálod a Ciphey összes hibáját! Javítsd ki őket és felkerülsz a közreműködők listájára ;)

# Alakítsd át a kódbázist
Ciphey nem minden része követi a PEP8 szabályzatot, és sok az ismétlődő kódrészlet.
