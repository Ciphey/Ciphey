"""
Not yet implemented.
"""
class letters:

    """Deals with Nato Strings / first letter of every word"""

    def __init__(self):
        None

    def __name__(self):
        return "Letters"

    def decrypt(self, text: str) -> dict:
        return text

    def first_letter_every_word(self, text):
        """
        This should be supplied a string like "hello my name is"
        """

        text = text.split(".")

        new_text = []
        for sentence in text:
            for word in sentence.split(" "):
                new_text.append(word[0])
            # Applies a space after every sentence
            # which might be every word
            new_text.append(" ")
