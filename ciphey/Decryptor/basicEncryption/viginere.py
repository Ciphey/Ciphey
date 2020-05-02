import itertools, re

try:
    import Decryptor.basicEncryption.freqAnalysis
except ModuleNotFoundError:
    import ciphey.Decryptor.basicEncryption.freqAnalysis


class Viginere:
    def __init__(self, lc):
        self.LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.SILENT_MODE = True  # If set to True, program doesn't print anything.
        self.NUM_MOST_FREQ_LETTERS = 4  # Attempt this many letters per subkey.
        self.MAX_KEY_LENGTH = 16  # Will not attempt keys longer than this.
        self.NONLETTERS_PATTERN = re.compile("[^A-Z]")

        self.lc = lc

    def main(self):
        # Instead of typing this ciphertext out, you can copy & paste it
        # from https://www.nostarch.com/crackingcodes/.
        ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""
        hackedMessage = self.hackVigenere(ciphertext)

        if hackedMessage != None:
            print("Copying hacked message to clipboard:")
            print(hackedMessage)
        else:
            print("Failed to hack encryption.")

    def decrypt(self, text):
        result = self.hackVigenere(text)
        if result["IsPlaintext?"]:
            return result
        else:
            return result

    def findRepeatSequencesSpacings(self, message):
        # Goes through the message and finds any 3 to 5 letter sequences
        # that are repeated. Returns a dict with the keys of the sequence and
        # values of a list of spacings (num of letters between the repeats).

        # Use a regular expression to remove non-letters from the message:
        message = self.NONLETTERS_PATTERN.sub("", message.upper())

        # Compile a list of seqLen-letter sequences found in the message:
        seqSpacings = {}  # Keys are sequences, values are lists of int spacings.
        for seqLen in range(3, 6):
            for seqStart in range(len(message) - seqLen):
                # Determine what the sequence is, and store it in seq:
                seq = message[seqStart : seqStart + seqLen]

                # Look for this sequence in the rest of the message:
                for i in range(seqStart + seqLen, len(message) - seqLen):
                    if message[i : i + seqLen] == seq:
                        # Found a repeated sequence.
                        if seq not in seqSpacings:
                            seqSpacings[seq] = []  # Initialize a blank list.

                        # Append the spacing distance between the repeated
                        # sequence and the original sequence:
                        seqSpacings[seq].append(i - seqStart)
        return seqSpacings

    def getUsefulFactors(self, num):
        # Returns a list of useful factors of num. By "useful" we mean factors
        # less than MAX_KEY_LENGTH + 1 and not 1. For example,
        # getUsefulFactors(144) returns [2, 3, 4, 6, 8, 9, 12, 16]

        if num < 2:
            return []  # Numbers less than 2 have no useful factors.

        factors = []  # The list of factors found.

        # When finding factors, you only need to check the integers up to
        # MAX_KEY_LENGTH.
        for i in range(2, self.MAX_KEY_LENGTH + 1):  # Don't test 1: it's not useful.
            if num % i == 0:
                factors.append(i)
                otherFactor = int(num / i)
                if otherFactor < self.MAX_KEY_LENGTH + 1 and otherFactor != 1:
                    factors.append(otherFactor)
        return list(set(factors))  # Remove duplicate factors.

    def getItemAtIndexOne(self, items):
        return items[1]

    def getMostCommonFactors(self, seqFactors):
        # First, get a count of how many times a factor occurs in seqFactors:
        factorCounts = {}  # Key is a factor, value is how often it occurs.

        # seqFactors keys are sequences, values are lists of factors of the
        # spacings. seqFactors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
        # 18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}
        for seq in seqFactors:
            factorList = seqFactors[seq]
            for factor in factorList:
                if factor not in factorCounts:
                    factorCounts[factor] = 0
                factorCounts[factor] += 1

        # Second, put the factor and its count into a tuple, and make a list
        # of these tuples so we can sort them:
        factorsByCount = []
        for factor in factorCounts:
            # Exclude factors larger than MAX_KEY_LENGTH:
            if factor <= self.MAX_KEY_LENGTH:
                # factorsByCount is a list of tuples: (factor, factorCount)
                # factorsByCount has a value like: [(3, 497), (2, 487), ...]
                factorsByCount.append((factor, factorCounts[factor]))

        # Sort the list by the factor count:
        factorsByCount.sort(key=self.getItemAtIndexOne, reverse=True)

        return factorsByCount

    def kasiskiExamination(self, ciphertext):
        # Find out the sequences of 3 to 5 letters that occur multiple times
        # in the ciphertext. repeatedSeqSpacings has a value like:
        # {'EXG': [192], 'NAF': [339, 972, 633], ... }
        repeatedSeqSpacings = self.findRepeatSequencesSpacings(ciphertext)

        # (See getMostCommonFactors() for a description of seqFactors.)
        seqFactors = {}
        for seq in repeatedSeqSpacings:
            seqFactors[seq] = []
            for spacing in repeatedSeqSpacings[seq]:
                seqFactors[seq].extend(self.getUsefulFactors(spacing))

        # (See getMostCommonFactors() for a description of factorsByCount.)
        factorsByCount = self.getMostCommonFactors(seqFactors)

        # Now we extract the factor counts from factorsByCount and
        # put them in allLikelyKeyLengths so that they are easier to
        # use later:
        allLikelyKeyLengths = []
        for twoIntTuple in factorsByCount:
            allLikelyKeyLengths.append(twoIntTuple[0])

        return allLikelyKeyLengths

    def getNthSubkeysLetters(self, nth, keyLength, message):
        # Returns every nth letter for each keyLength set of letters in text.
        # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
        #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
        #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
        #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

        # Use a regular expression to remove non-letters from the message:
        message = self.NONLETTERS_PATTERN.sub("", message)

        i = nth - 1
        letters = []
        while i < len(message):
            letters.append(message[i])
            i += keyLength
        return "".join(letters)

    def attemptHackWithKeyLength(self, ciphertext, mostLikelyKeyLength):
        # Determine the most likely letters for each letter in the key:
        ciphertextUp = ciphertext.upper()
        # allFreqScores is a list of mostLikelyKeyLength number of lists.
        # These inner lists are the freqScores lists.
        allFreqScores = []
        for nth in range(1, mostLikelyKeyLength + 1):
            nthLetters = self.getNthSubkeysLetters(
                nth, mostLikelyKeyLength, ciphertextUp
            )

            # freqScores is a list of tuples like:
            # [(<letter>, <Eng. Freq. match score>), ... ]
            # List is sorted by match score. Higher score means better match.
            # See the englishFreqMatchScore() comments in freqAnalysis.py.
            freqScores = []
            for possibleKey in self.LETTERS:
                decryptedText = self.decryptMessage(possibleKey, nthLetters)
                keyAndFreqMatchTuple = (
                    possibleKey,
                    Decryptor.basicEncryption.freqAnalysis.englishFreqMatchScore(
                        decryptedText
                    ),
                )
                freqScores.append(keyAndFreqMatchTuple)
            # Sort by match score:
            freqScores.sort(key=self.getItemAtIndexOne, reverse=True)

            allFreqScores.append(freqScores[: self.NUM_MOST_FREQ_LETTERS])

        if not self.SILENT_MODE:
            for i in range(len(allFreqScores)):
                # Use i + 1 so the first letter is not called the "0th" letter:
                print("Possible letters for letter %s of the key: " % (i + 1), end="")
                for freqScore in allFreqScores[i]:
                    print("%s " % freqScore[0], end="")
                print()  # Print a newline.

        # Try every combination of the most likely letters for each position
        # in the key:
        for indexes in itertools.product(
            range(self.NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength
        ):
            # Create a possible key from the letters in allFreqScores:
            possibleKey = ""
            for i in range(mostLikelyKeyLength):
                possibleKey += allFreqScores[i][indexes[i]][0]

            if not self.SILENT_MODE:
                print("Attempting with key: %s" % (possibleKey))

            decryptedText = self.decryptMessage(possibleKey, ciphertextUp)

            if self.lc.checkLanguage(decryptedText):
                # Set the hacked ciphertext to the original casing:
                origCase = []
                for i in range(len(ciphertext)):
                    if ciphertext[i].isupper():
                        origCase.append(decryptedText[i].upper())
                    else:
                        origCase.append(decryptedText[i].lower())
                decryptedText = "".join(origCase)

                # Check with user to see if the key has been found:
                return {
                    "lc": self.lc,
                    "IsPlaintext?": True,
                    "Plaintext": decryptedText,
                    "Cipher": "Viginere",
                    "Extra Information": f"The key used is {possibleKey}",
                }

        # No English-looking decryption found, so return None:
        return None

    def hackVigenere(self, ciphertext):
        # First, we need to do Kasiski Examination to figure out what the
        # length of the ciphertext's encryption key is:
        allLikelyKeyLengths = self.kasiskiExamination(ciphertext)
        if not self.SILENT_MODE:
            keyLengthStr = ""
            for keyLength in allLikelyKeyLengths:
                keyLengthStr += "%s " % (keyLength)
            print(
                "Kasiski Examination results say the most likely key lengths are: "
                + keyLengthStr
                + "\n"
            )
        hackedMessage = None
        for keyLength in allLikelyKeyLengths:
            if not self.SILENT_MODE:
                print(
                    "Attempting hack with key length %s (%s possible keys)..."
                    % (keyLength, self.NUM_MOST_FREQ_LETTERS ** keyLength)
                )
            hackedMessage = self.attemptHackWithKeyLength(ciphertext, keyLength)
            if hackedMessage != None:
                break

        # If none of the key lengths we found using Kasiski Examination
        # worked, start brute-forcing through key lengths:
        if hackedMessage == None:
            if not self.SILENT_MODE:
                print(
                    "Unable to hack message with likely key length(s). Brute forcing key length..."
                )
            for keyLength in range(1, self.MAX_KEY_LENGTH + 1):
                # Don't re-check key lengths already tried from Kasiski:
                if keyLength not in allLikelyKeyLengths:
                    if not self.SILENT_MODE:
                        print(
                            "Attempting hack with key length %s (%s possible keys)..."
                            % (keyLength, self.NUM_MOST_FREQ_LETTERS ** keyLength)
                        )
                    hackedMessage = self.attemptHackWithKeyLength(ciphertext, keyLength)
                    if hackedMessage != None:
                        break
        return hackedMessage

    def decryptMessage(self, key, message):
        return self.translateMessage(key, message, "decrypt")

    def getName(self):
        return "Viginere"

    def translateMessage(self, key, message, mode):
        translated = []  # Stores the encrypted/decrypted message string.

        keyIndex = 0
        key = key.upper()

        for symbol in message:  # Loop through each symbol in message.
            num = self.LETTERS.find(symbol.upper())
            if num != -1:  # -1 means symbol.upper() was not found in LETTERS.
                if mode == "encrypt":
                    num += self.LETTERS.find(key[keyIndex])  # Add if encrypting.
                elif mode == "decrypt":
                    num -= self.LETTERS.find(key[keyIndex])  # Subtract if decrypting.

                num %= len(self.LETTERS)  # Handle any wraparound.

                # Add the encrypted/decrypted symbol to the end of translated:
                if symbol.isupper():
                    translated.append(self.LETTERS[num])
                elif symbol.islower():
                    translated.append(self.LETTERS[num].lower())

                keyIndex += 1  # Move to the next letter in the key.
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # Append the symbol without encrypting/decrypting.
                translated.append(symbol)

        return "".join(translated)


# If vigenereHacker.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    v = Viginere()
    v.main()
