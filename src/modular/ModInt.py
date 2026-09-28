
class ModInt:
    def __init__(self, words: list[int], radix: int, mod: int):
        self.words = words
        self.radix = radix
        self.mod = mod