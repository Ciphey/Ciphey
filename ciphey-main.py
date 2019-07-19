"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt
"""
import LanguageChecker
class Ciphey:
    def __init__(self):
        print("hello!")
        parser = argparse.ArgumentParser(description='Blog')
        parser.add_argument('-f','--file', help='File you want to decrypt', required=False)
        parser.add_argument('-l','--level', help='How many levels of decryption you want (the more levels, the slower it is)', required=False)
        args = vars(parser.parse_args())
        LanguageChecker.chisquare("hello this is a test I hope you have a good day")