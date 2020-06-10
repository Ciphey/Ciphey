import itertools, re
import cipheycore
import cipheydists


class Vigenere:
    def __init__(self, lc):
        self.LETTERS = "abcdefghijklmnopqrstuvwxyz"
        self.SILENT_MODE = True  # If set to True, program doesn't print anything.
        self.NUM_MOST_FREQ_LETTERS = 4  # Attempt this many letters per subkey.
        self.MAX_KEY_LENGTH = 16  # Will not attempt keys longer than this.
        self.NONLETTERS_PATTERN = re.compile("[^A-Z]")

        self.lc = lc

    def decrypt(self, text):
        result = self.hackVigenere(text)
        if result is None:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": "Viginere",
                "Extra Information": None,
            }

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

    def attemptHackWithKeyLength(self, ciphertext, mostLikelyKeyLength):
        # Determine the most likely letters for each letter in the key:
        ciphertext = ciphertext.lower()

        # Do core work
        group = cipheydists.get_charset("english")["lcase"]
        expected = cipheydists.get_dist("lcase")
        possible_keys = cipheycore.vigenere_crack(
            ciphertext, expected, group, mostLikelyKeyLength
        )
        n_keys = len(possible_keys)

        # Try all the feasible keys
        for candidate in possible_keys:
            nice_key = list(candidate.key)
            # Create a possible key from the letters in allFreqScores:
            if not self.SILENT_MODE:
                print("Attempting with key: %s" % nice_key)

            decryptedText = cipheycore.vigenere_decrypt(
                ciphertext, candidate.key, group
            )

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
                    "Extra Information": f"The key used is {nice_key}",
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

    def getName(self):
        return "Viginere"

