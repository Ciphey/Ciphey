from typing import Optional, Dict, List
from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry


@registry.register_multi((str, str), (bytes, bytes))
class Rot47Decoder(Decoder[str, str]):
    """
    This class includes the ROT47 decoder
    """
    def decode(self, ctext: T) -> Optional[U]:
        """
        The decoder function for the ROT47 algorithm

        :param ctext: The input ciphertext
        :return: The decoded string from the ciphertext
        """
        # The ciphertext will be encoded using a ROT47 alphabet, here, named encode_alphabet
        encode_alphabet = '!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ '

        # The decoder_alphabet can reserve the cipher and turn it into the plaintext
        decoder_alphabet = 'PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO '

        # Uniting both alphabets, we get the decoding key
        decoder_dict = dict(zip(encode_alphabet, decoder_alphabet))

        # From all the words of the ciphertext, we tokenize every letter for easy retrieval from the dictionary
        encrypted_words = list(ctext)
        # Empty string in which the plaintext will be concatenated
        decoded_words = ''

        # We get the values from the dictionary, and build back the plaintext
        for character in encrypted_words:
            decoded_words += decoder_dict.get(character)

        # Return the plaintext
        return decoded_words

    @staticmethod
    def priority() -> float:
        """
        Set to pretty low
        :return:
        """
        return 0.5

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        """
        Adds the alphabet dictionary
        :return:
        """
        return {
            "dict": ParamSpec(
                desc="The ROT47 alphabet dictionary to use",
                req=False,
                default="cipheydists::translate::rot47",
            )
        }

    @staticmethod
    def getTarget() -> str:
        """
        Type of decoder
        :return:
        """
        return "rot47_decoder"

