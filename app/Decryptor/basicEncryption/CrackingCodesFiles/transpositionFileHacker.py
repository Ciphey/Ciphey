# Transposition File Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import time, os, sys, transpositionDecrypt, detectEnglish

inputFilename = 'frankenstein.encrypted.txt'
outputFilename = 'frankenstein.decrypted.txt'

def main():
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting.' % (inputFilename))
        sys.exit()

    inputFile = open(inputFilename)
    content = inputFile.read()
    inputFile.close()

    hackedMessage = hackTransposition(content)

    if hackedMessage != None:
        print('Writing decrypted text to %s.' % (outputFilename))

        outputFile = open(outputFilename, 'w')
        outputFile.write(hackedMessage)
        outputFile.close()
    else:
        print('Failed to hack encryption.')


# The hackTransposition() function's code was copy/pasted from
# transpositionHacker.py and had some modifications made.
def hackTransposition(message):
    print('Hacking...')
    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    for key in range(1, len(message)):
        print('Trying key #%s... ' % (key), end='')
        sys.stdout.flush()

        # We want to track the amount of time it takes to test a single key,
        # so we record the time in startTime.
        startTime = time.time()

        decryptedText = transpositionDecrypt.decryptMessage(key, message)
        englishPercentage = round(detectEnglish.getEnglishCount(decryptedText) * 100, 2)

        totalTime = round(time.time() - startTime, 3)
        print('Test time: %s seconds, ' % (totalTime), end='')
        sys.stdout.flush() # Flush printed text to the screen.

        print('Percent English: %s%%' % (englishPercentage))
        if englishPercentage > 20:
            print()
            print('Key ' + str(key) + ': ' + decryptedText[:100])
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


# If transpositionFileHacker.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()