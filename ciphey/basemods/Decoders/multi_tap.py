from typing import Optional, Dict, List

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry


@registry.register_multi((str, str), (bytes, bytes))
class multiTap(Decoder[str, str]):
    def decode(self, ctext: str) -> Optional[str]:
        decode_text = ""
        for x in multiTap.split_the_text(ctext):
            if not x.isdigit() or len(set(x)) != 1:
                return None
            if x == "0":  # if it space
                decode_text += " "
            elif multiTap.valid_code_part(ctext):
                decode_text += self.number_to_char(x)

        return decode_text

    @staticmethod
    def split_the_text(text):
        return text.split()

    @staticmethod
    def valid_code_part(code):
        try:
            return int(code[0]) in range(2, 10)
        except ValueError:
            return False

    @staticmethod
    def number_to_char(number: str) -> str:
        index = multiTap.calculate_index(number)
        return multiTap.number_index_to_char(index)

    @staticmethod
    def number_index_to_char(index_number: int) -> str:
        start_ascii_value = ord("A")
        return chr(start_ascii_value + index_number)

    @staticmethod
    def calculate_index(number: str) -> int:
        first_number_as_int = int(number[0])

        number_index = multiTap.get_index_from_first_digit(first_number_as_int)

        num_rest_numbers = len(number) - 1
        number_index += num_rest_numbers

        return number_index

    @staticmethod
    def get_index_from_first_digit(first_digit):
        number_index = 0
        if first_digit >= 8:  # s have 4 chars
            number_index += 1

        first_digit -= 2  # start in 200

        number_index += first_digit * 3  # jump 3 every time

        return number_index

    @staticmethod
    def priority() -> float:
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "Multi-tap"
