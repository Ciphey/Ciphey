from typing import Optional, Dict, List
from ciphey.iface import ParamSpec, Config, Decoder, registry


@registry.register_multi((str, str), (bytes, bytes))
class Baconian(Decoder[str, str]):

    lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
    
    lookup_default = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaaa', 
        'K':'abaab', 'L':'ababa', 'M':'ababb', 'N':'abbaa', 'O':'abbab', 
        'P':'abbba', 'Q':'abbbb', 'R':'baaaa', 'S':'baaab', 'T':'baaba', 
        'U':'baabb', 'V':'baabb', 'W':'babaa', 'X':'babab', 'Y':'babba', 'Z':'babbb'}



    def decode(self, ctext: str) -> Optional[str]:
        """
        Performs Baconian decoding
        """
        i = 0
        
        default_decoced_string = ""
        decoced_string = ""

        return_default_string = True
        while True:
            if(i < len(ctext)-4): 
                substr = ctext[i:i + 5] 
                if(substr[0] != ' '):
                    decoced_string += list(self.lookup.keys())[list(self.lookup.values()).index(substr)]

                    if return_default_string:
                        index = list(self.lookup_default.values()).index(substr)
                        if index:
                            default_decoced_string += list(self.lookup_default.keys())[index]
                        else:
                            return_default_string = False 
                    i += 5
                else: 
                    default_decoced_string += ' '
                    decoced_string += ' '
                    i += 1
            else: 
                break
        
        if return_default_string:
            return default_decoced_string
        else:
            return decoced_string



    @staticmethod
    def priority() -> float:
        return 0.025

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "baconian"