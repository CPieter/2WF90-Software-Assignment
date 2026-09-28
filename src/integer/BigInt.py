
DIGITS = "0123456789ABCDEF"

class BigInt:
    def __init__(self, words: list[int], radix: int, negative: bool = False):
        if not 2 <= radix <= 16:
            raise ValueError("Radix must be between 2 and 16")
        if not words or any(digit < 0 or digit >= radix for digit in words):
            raise ValueError("Invalid digits for this radix")
        
        self.words = words.copy()
        while len (self.words) > 1 and self.words[-1] == 0:
            self.words.pop()
        self.radix = radix
        self.negative = negative and not self.is_zero()
        
    @classmethod
    def from_string(cls, value: str, radix: int) -> "BigInt":
        if not value:
            raise ValueError("The number cannot be empty")
        negative = value[0] == "-"
        digits = value[1:] if negative else value
        if not digits:
            raise ValueError("A sign must be followed by a digit")
        
        words = []
        for character in reversed(digits):
            digit = DIGITS.find(character.upper())
            if digit < 0 or digit >= radix:
                raise ValueError("Invalid digit")
            words.append(digit)
        return cls(words, radix, negative)
    
    def to_string(self) -> str:
        digits = "".join(DIGITS[digit] for digit in reversed(self.words))
        return "-" + digits if self.negative else digits
    
    def is_zero(self) -> bool:
        return self.words == [0]
    
    def compare_magnitude(self, other: "BigInt") -> int:
        if self.radix != other.radix:
            raise ValueError("numbers must use the same radix")
        if len(self.words) != len(other.words):
            return 1 if len(self.words) > len(other.words) else -1
        for i in range(len(self.words) - 1, -1, -1):
            if self.words[i] != other.words[i]:
                return 1 if self.words[i] > other.words[i] else -1
        return 0
    
    def __neg__(self) -> "BigInt":
        return BigInt(self.words, self.radix, not self.negative)
    
    def __add__(self, other: "BigInt") -> "BigInt":
        from src.integer.addition import add
        return add(self, other)
    
    def __sub__(self, other: "BigInt") -> "BigInt":
        from src.integer.subtraction import subtract
        return subtract(self, other)
    
    def __str__(self) -> str:
        return self.to_string()
        
        
    
    
        
        