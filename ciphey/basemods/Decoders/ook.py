from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry, Translation

from loguru import logger


@registry.register
class Ook(Decoder[str, str]):
    """
    Ook is an esoteric language that is just an obfuscation of Brainfuck.
    The language consists of three atomics, 'Ook.', 'Ook!' and 'Ook?', which in different combinations yield
    the characters of the brainfuck language.
    """

    def decode(self, ctext: str) -> Optional[str]:
        """
        Performs Ook -> Brainfuck conversion
        """
        logger.trace("Attempting Ook decoding")
        # Convert newlines to whitespace
        ctext = ctext.replace('\n'," ").replace('\r\n'," ")
        # Only valid statements in Ook are 'Ook.', 'Ook!' and 'Ook?'
        # Since we are passing this on to Brainfuck, we are very strict with what a valid Ook text looks like
        valid_statements = ["Ook.", "Ook!", "Ook?"]
        all_statements = ctext.split() 
        logger.debug(f"All ook statements: {all_statements}")
        if any([x not in valid_statements for x in all_statements]):
            logger.debug("Ignoring ctext because there were non-Ook statements in input text")
            return None
        
        # If there is an od number of statements, this can't be valid Ook since every Ook statement comes in pairs
        if len(all_statements) % 2 == 1:
            logger.debug("Ignoring since there were an odd number of Ook statements in input text")
            return None

        # Remove this 
        self.translate = {
            "Ook. Ook.": "+",
            "Ook! Ook!": "-",
            "Ook. Ook?": ">",
            "Ook? Ook.": "<",
            "Ook! Ook?": "[",
            "Ook? Ook!": "]",
            "Ook! Ook.": ".",
            "Ook. Ook!": "," 
        }
        
        # This will generate pairs of statements, discarding the last item if there is an odd number of items.
        # Then, convert it back to a single string. 
        # This makes it so that pairs of Ook statements have whitespace between, while non-pairs don't have whitespace
        # For instance, if the statement is ["Ook.", "Ook.", "Ook! Ook."], the resulting output is "Ook. Ook.Ook! Ook."
        pairs = zip(all_statements[::2], all_statements[1::2])
        ctext = ''.join(map(' '.join, pairs))
        logger.debug(f"Converted input ctext to {ctext}")
        for src, dst in self.translate.items():
            ctext = ctext.replace(src, dst)
        logger.debug(f"Brainfuck decoded text after Ook decoding: {ctext}")
        # If there are any remaining Ook statements in the text, it means that there was an illegal pair of Ook statements.
        # For instance, Ook? Ook? is not a valid statement.
        input()
        return None if "Ook" in ctext else ctext

    @staticmethod
    def priority() -> float:
        return 0.01

    def __init__(self, config: Config):
        super().__init__(config)
        #self.translate = config.get_resource(self._params()["dict"], Translation)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The ook dictionary to use",
                req=False,
                default="cipheydists::translate::ook",
            )
        }

    @staticmethod
    def getTarget() -> str:
        return "ook"
