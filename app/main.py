"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt
"""
import languageChecker.LanguageChecker
import neuralnetwork.nn
class Ciphey:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Blog')
        parser.add_argument('-f','--file', help='File you want to decrypt', required=False)
        parser.add_argument('-l','--level', help='How many levels of decryption you want (the more levels, the slower it is)', required=False)
        parser.add_argument('-g','--greppable', help='Are you grepping this output?', required=False)

        args = vars(parser.parse_args())
        print("""
        ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
        ██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
        ██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
        ██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
        ╚██████╗██║██║     ██║  ██║███████╗   ██║ """)
        self.ai = nn()
    