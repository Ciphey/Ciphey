from typing import Optional, Dict, List

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry


@registry.register
class multiTap(Decoder[str, str]):
    def decode(self, ctext: str) -> Optional[str]:
        decode_text = ""
        for x in ctext.split():
            if x == self.SPACE_DIGIT:  # check if it space
                decode_text += " "
            elif not multiTap.valid_code_part(x):
                return None
            else:
                decode_text += self.decode_num_to_char(x)

        return decode_text

    @staticmethod
    def valid_code_part(code: str) -> bool:
        if not code.isdigit():
            return False

        # if not all the digits are the same
        if not multiTap.is_all_dup(code):
            return False

        if int(code[0]) not in range(2, 10):
            return False

        if len(code) > 4:
            return False

        return True

    @staticmethod
    def decode_num_to_char(number: str) -> str:
        index = multiTap.calculate_index(number)
        return multiTap.number_index_to_char(index)

    @staticmethod
    def is_all_dup(code):
        return len(set(code)) == 1

    @staticmethod
    def calculate_index(number: str) -> int:
        first_number_as_int = int(number[0])

        number_index = multiTap.get_index_from_first_digit(first_number_as_int)

        # add to index the number of the char : "22" -> index += 1
        num_rest_numbers = len(number) - 1
        number_index += num_rest_numbers

        return number_index

    @staticmethod
    def number_index_to_char(index_number: int) -> str:
        start_ascii_value = ord("A")
        return chr(start_ascii_value + index_number)

    @staticmethod
    def get_index_from_first_digit(first_digit: int) -> int:
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
        self.SPACE_DIGIT = "0"

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "Multi-tap"
