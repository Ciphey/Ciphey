class Viginere:
    def __init__(self, lc):
        self.lc = lc
        self.MAX_KEY_LENGTH = 16
        self.self.NONself.LETTERS_PATTERN = re.compile('[^A-Z]')
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.analysis = ""
    def decrypt(self, text):
        result = hackVigenere(text)
        print(result)
        if result['IsPlaintext?']:
            return result
        else:
            return {"lc": self.lc, "IsPlaintext?": False, "Plaintext": None, "Cipher": "Vigenère cipher", "Extra Information": f"{self.analysis}"}

    def findRepeatSequencesSpacings(self, message):
        
        # Goes through the message and finds any 3 to 5 letter sequences
        # that are repeated. Returns a dict with the keys of the sequence and
        # values of a list of spacings (num of self.LETTERS between the repeats).
    
        # Use a regular expression to remove non-self.LETTERS from the message:
        message = self.NONself.LETTERS_PATTERN.sub('', message.upper())
    
        # Compile a list of seqLen-letter sequences found in the message:
        seqSpacings = {} # Keys are sequences, values are lists of int spacings.
        for seqLen in range(3, 6):
            for seqStart in range(len(message) - seqLen):
                # Determine what the sequence is, and store it in seq:
                seq = message[seqStart:seqStart + seqLen]
    
                # Look for this sequence in the rest of the message:
                for i in range(seqStart + seqLen, len(message) - seqLen):
                    if message[i:i + seqLen] == seq:
                        # Found a repeated sequence.
                        if seq not in seqSpacings:
                            seqSpacings[seq] = [] # Initialize a blank list.
    
                        # Append the spacing distance between the repeated
                        # sequence and the original sequence:
                        seqSpacings[seq].append(i - seqStart)
        return seqSpacings
    def getUsefulFactors(self, num):
         # Will not attempt keys longer than this.
        # Returns a list of useful factors of num. By "useful" we mean factors
        # less than self.MAX_KEY_LENGTH + 1 and not 1. For example,
        # getUsefulFactors(144) returns [2, 3, 4, 6, 8, 9, 12, 16]
    
        if num < 2:
            return [] # Numbers less than 2 have no useful factors.
    
        factors = [] # The list of factors found.
    
        # When finding factors, you only need to check the integers up to
        # self.MAX_KEY_LENGTH.
        for i in range(2, self.MAX_KEY_LENGTH + 1): # Don't test 1: it's not useful.
            if num % i == 0:
                factors.append(i)
                otherFactor = int(num / i)
                if otherFactor < self.MAX_KEY_LENGTH + 1 and otherFactor != 1:
                    factors.append(otherFactor)
        return list(set(factors)) # Remove duplicate factors.
    def getItemAtIndexOne(self, items):
        return items[1]
    def getMostCommonFactors(self, seqFactors):
        # First, get a count of how many times a factor occurs in seqFactors:
        factorCounts = {} # Key is a factor, value is how often it occurs.
    
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
            # Exclude factors larger than self.MAX_KEY_LENGTH:
            if factor <= self.MAX_KEY_LENGTH:
                # factorsByCount is a list of tuples: (factor, factorCount)
                # factorsByCount has a value like: [(3, 497), (2, 487), ...]
                factorsByCount.append( (factor, factorCounts[factor]) )
    
        # Sort the list by the factor count:
        factorsByCount.sort(key=getItemAtIndexOne, reverse=True)
    
        return factorsByCount
    def kasiskiExamination(self, ciphertext):
        # Find out the sequences of 3 to 5 self.LETTERS that occur multiple times
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
        # Returns every nth letter for each keyLength set of self.LETTERS in text.
        # E.g. getNthSubkeysself.LETTERS(1, 3, 'ABCABCABC') returns 'AAA'
        #      getNthSubkeysself.LETTERS(2, 3, 'ABCABCABC') returns 'BBB'
        #      getNthSubkeysself.LETTERS(3, 3, 'ABCABCABC') returns 'CCC'
        #      getNthSubkeysself.LETTERS(1, 5, 'ABCDEFGHI') returns 'AF'
    
        # Use a regular expression to remove non-self.LETTERS from the message:
        message = self.NONself.LETTERS_PATTERN.sub('', message)
    
        i = nth - 1
        self.LETTERS = []
        while i < len(message):
            self.LETTERS.append(message[i])
            i += keyLength
        return ''.join(self.LETTERS)
    def attemptHackWithKeyLength(self, ciphertext, mostLikelyKeyLength):
        # Determine the most likely self.LETTERS for each letter in the key:
        ciphertextUp = ciphertext.upper()
        # allFreqScores is a list of mostLikelyKeyLength number of lists.
        # These inner lists are the freqScores lists.
        allFreqScores = []
        for nth in range(1, mostLikelyKeyLength + 1):
            nthself.LETTERS = self.getNthSubkeysself.LETTERS(nth, mostLikelyKeyLength, ciphertextUp)
    
            # freqScores is a list of tuples like:
            # [(<letter>, <Eng. Freq. match score>), ... ]
            # List is sorted by match score. Higher score means better match.
            # See the englishFreqMatchScore() comments in freqAnalysis.py.
            freqScores = []
            for possibleKey in self.LETTERS:
                decryptedText = vigenereCipher.decryptMessage(possibleKey, nthself.LETTERS)
                keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
                freqScores.append(keyAndFreqMatchTuple)
            # Sort by match score:
            freqScores.sort(key=getItemAtIndexOne, reverse=True)
    
            allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

        # Try every combination of the most likely self.LETTERS for each position
        # in the key:
        for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
            # Create a possible key from the self.LETTERS in allFreqScores:
            possibleKey = ''
            for i in range(mostLikelyKeyLength):
                possibleKey += allFreqScores[i][indexes[i]][0]
    
            decryptedText = vigenereCipher.decryptMessage(possibleKey, ciphertextUp)
    
            if self.lc.checkLanguage(translated):
                # Set the hacked ciphertext to the original casing:
                origCase = []
                for i in range(len(ciphertext)):
                    if ciphertext[i].isupper():
                        origCase.append(decryptedText[i].upper())
                    else:
                        origCase.append(decryptedText[i].lower())
                decryptedText = ''.join(origCase)
            
                return {"lc": self.lc, "IsPlaintext?": True, "Plaintext": decryptedText, "Cipher": "Vigenère cipher", "Extra Information": f"{self.analysis}. The key used is {possibleKey}"}
    
        # No English-looking decryption found, so return None:
        return None
    def hackVigenere(self, ciphertext):
        # First, we need to do Kasiski Examination to figure out what the
        # length of the ciphertext's encryption key is:
        allLikelyKeyLengths = kasiskiExamination(ciphertext)
        if not SILENT_MODE:
            keyLengthStr = ''
            for keyLength in allLikelyKeyLengths:
                keyLengthStr += '%s ' % (keyLength)
            self.analysis = f'Kasiski Examination results say the most likely key lengths are {keyLengthStr}'
        hackedMessage = None
        for keyLength in allLikelyKeyLengths:
            hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
            if hackedMessage != None:
                break
    
        # If none of the key lengths we found using Kasiski Examination
        # worked, start brute-forcing through key lengths:
        if hackedMessage == None:
            for keyLength in range(1, MAX_KEY_LENGTH + 1):
                # Don't re-check key lengths already tried from Kasiski:
                if keyLength not in allLikelyKeyLengths:
                    # First, we need to do Kasiski Examination to figure out what the
                    # length of the ciphertext's encryption key is:
                    allLikelyKeyLengths = kasiskiExamination(ciphertext)
                    if not SILENT_MODE:
                        keyLengthStr = ''
                        for keyLength in allLikelyKeyLengths:
                            keyLengthStr += '%s ' % (keyLength)
                    hackedMessage = None
                    for keyLength in allLikelyKeyLengths:
                        hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
                        if hackedMessage != None:
                            break
                
                    # If none of the key lengths we found using Kasiski Examination
                    # worked, start brute-forcing through key lengths:
                    if hackedMessage == None:
                        for keyLength in range(1, MAX_KEY_LENGTH + 1):
                            # Don't re-check key lengths already tried from Kasiski:
                            if keyLength not in allLikelyKeyLengths:
                                hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
                                if hackedMessage != None:
                                    break
                    return hackedMessage
                    hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
                    if hackedMessage != None:
                        break
        return hackedMessage
    def encryptMessage(self, key, message):
        return translateMessage(key, message, 'encrypt')
    
    
    def decryptMessage(self, key, message):
        return translateMessage(key, message, 'decrypt')
    def translateMessage(self, key, message, mode):
        translated = [] # Stores the encrypted/decrypted message string.
    
        keyIndex = 0
        key = key.upper()
    
        for symbol in message: # Loop through each symbol in message.
            num = self.LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in self.LETTERS.
                if mode == 'encrypt':
                    num += self.LETTERS.find(key[keyIndex]) # Add if encrypting.
                elif mode == 'decrypt':
                    num -= self.LETTERS.find(key[keyIndex]) # Subtract if decrypting.
    
                num %= len(self.LETTERS) # Handle any wraparound.
    
                # Add the encrypted/decrypted symbol to the end of translated:
                if symbol.isupper():
                    translated.append(self.LETTERS[num])
                elif symbol.islower():
                    translated.append(self.LETTERS[num].lower())
    
                keyIndex += 1 # Move to the next letter in the key.
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # Append the symbol without encrypting/decrypting.
                translated.append(symbol)
    
        return ''.join(translated)