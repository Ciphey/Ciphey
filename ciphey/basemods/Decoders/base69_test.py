from math import floor, ceil


class Base69:

    def byte_to_chars(self, n: int):
        return f'{self.CHARS[n % 69]}{self.CHARS[floor(n / 69)]}'

    def chars_to_byte(self, s: str):
        print(f'c2b received {s} and returns {(69 * self.CHARS.index(s[1])) + (self.CHARS.index(s[0]))}')
        return (69 * self.CHARS.index(s[1])) + (self.CHARS.index(s[0]))

    def decode_chunk(self, s: str):
        padded_bytes = s.endswith('=')
        decoded = [0 for _ in range(8)]
        for i in range(8):
            decoded[i] = 0 if i == 7 and padded_bytes else self.chars_to_byte(s[ i * 2 : i * 2 + 2 ])
            print(f'decoded[{i}] = {decoded[i]}')
        result = [0 for _ in range(7)]
        for i in range(7):
            t1 = decoded[i] << (i + 1)
            print(f't1 = {decoded[i]} << {(i + 1)}')
            print(f't1 is {t1}')
            t2 = decoded[i + 1] >> (7 - i - 1)
            print(f't2 is {t2}')
            print(f't2 = {decoded[i + 1]} >> {(7 - i - 1)}')
            result[i] = t1 | t2
            print(f'result[{i}] = {t1 | t2}')
        return result

    def decode(self, ctext: str = 'gALBoAUAKAFACA*A'):
        """
        Performs Base69 decoding
        """
        extra_bytes = 0
        clen = len(ctext)
        if ctext[:-1] == '=':
            extra_bytes = int(ctext[clen - 2])
        CHUNK_COUNT = ceil(clen / 16)
        result = [0 for _ in range(CHUNK_COUNT * 7 - extra_bytes)]
        for i in range(CHUNK_COUNT):
            chunk_string = ctext[i * 16 : (i + 1) * 16]
            if extra_bytes and (i == CHUNK_COUNT - 1):
                insert = self.decode_chunk(chunk_string)
                for n, elem in enumerate(insert[0 : 7 - extra_bytes]):
                    result[n + i * 7] = elem
            else:
                insert = self.decode_chunk(chunk_string)
                for n, elem in enumerate(insert):
                    result[n + i * 7] = elem

        print(result)
        return bytearray(result).decode()


    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.05

    def __init__(self):
        self.CHARS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/-*<>|') # To be moved to CipheyDists
