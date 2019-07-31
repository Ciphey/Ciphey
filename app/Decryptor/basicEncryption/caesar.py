class caesar(ciphey):
    def __init__(self, message):
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.message = message
    def bruteFoce(self):
        for key in range(len(self.LETTERS)):
            translated = ''

            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key

                    if num < 0:
                        num = num + LETTERS[num]
                    
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol

                # TODO check translated for english

