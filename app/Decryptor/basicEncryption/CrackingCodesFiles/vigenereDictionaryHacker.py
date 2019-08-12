# Vigenere Cipher Dictionary Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import detectEnglish, vigenereCipher, pyperclip

def main():
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackVigenereDictionary(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip() # Remove the newline at the end.
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            # Check with user to see if the decrypted key has been found:
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()
