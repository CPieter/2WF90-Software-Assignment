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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BigInt) or self.radix != other.radix:
            return False
        if self.is_zero() and other.is_zero():
            return True
        return self.negative == other.negative and self.words == other.words

    def __lt__(self, other: "BigInt") -> bool:
        if not isinstance(other, BigInt):
            return NotImplemented
        if self.radix != other.radix:
            raise ValueError("Radices must match")

        if self.is_zero() and other.is_zero():
            return False
        if self.negative != other.negative:
            return self.negative

        mag = self.compare_magnitude(other)
        return mag < 0 if not self.negative else mag > 0

    def __le__(self, other: "BigInt") -> bool:
        return self < other or self == other

    def __gt__(self, other: "BigInt") -> bool:
        return not (self <= other)

    def __ge__(self, other: "BigInt") -> bool:
        return not (self < other)

    def __ne__(self, other: object) -> bool:
        return not (self == other)

    def __neg__(self) -> "BigInt":
        return BigInt(self.words, self.radix, not self.negative)
    
    def __add__(self, other: "BigInt") -> "BigInt":
        from src.integer.addition import add
        return add(self, other)
    
    def __sub__(self, other: "BigInt") -> "BigInt":
        from src.integer.subtraction import subtract
        return subtract(self, other)

    def __mul__(self, other: "BigInt") -> "BigInt":
        from src.integer.multiplication_primary import multiply_primary
        from src.integer.multiplication_karatsuba import multiply_karatsuba

        if min(len(self.words), len(other.words)) < 32:
            return multiply_primary(self, other)
        return multiply_karatsuba(self, other)

    def __abs__(self) -> "BigInt":
        return BigInt(self.words, self.radix, False)

    def __divmod__(self, other: "BigInt") -> tuple["BigInt", "BigInt"]:
        from src.integer.division import divmod_bigint
        return divmod_bigint(self, other)

    def __floordiv__(self, other: "BigInt") -> "BigInt":
        return divmod(self, other)[0]

    def __mod__(self, other: "BigInt") -> "BigInt":
        return divmod(self, other)[1]
    
    def __str__(self) -> str:
        return self.to_string()
        
        
    
    
        
        