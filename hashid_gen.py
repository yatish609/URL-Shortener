import random

class IDGenerator(object):
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"

    def __init__(self, length=8):
        self._alphabet_length = len(self.ALPHABET)
        self._id_length = length

    def _encode_int(self, n):
        encoded = ''
        while n > 0:
            n, r = divmod(n, self._alphabet_length)
            encoded = self.ALPHABET[r] + encoded
        return encoded

    def generate_id(self):
        start = self._alphabet_length**(self._id_length - 1)
        end = self._alphabet_length**self._id_length - 1
        return self._encode_int(random.randint(start, end))

if __name__ == "__main__":
    # Sample usage: Generate ten IDs each eight characters in length.
    idgen = IDGenerator(8)

    for i in range(10):
        print(idgen.generate_id())