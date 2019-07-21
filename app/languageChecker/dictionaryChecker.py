class dictionaryChecker:
    def __init__(self):
        None
    def checkDictionary(self, text, language):
        """Compares a word with 
        The dictionary is sorted and the text is sorted"""
        # reads through most common words / passwords
        # and calculates how much of that is in English
        text = text.split(" ")
        text = text.sort()
        # can dynamically use languages then
        language = str(language) + ".txt"
        f = open("english.txt", "r")
        f = f.readlines()
        counter = 0.00
        # dictionary is "word\n" so I remove the "\n"
        for word[0:-2] in f:
            if word == text:
                counter = counter + 1
        counter = mh.percentage(counter, len(text))
        return(counter)
    