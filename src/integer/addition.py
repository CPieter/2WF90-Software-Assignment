from src.integer.BigInt import BigInt
from src.integer.subtraction import subtract_magnitudes

def add(x: BigInt, y: BigInt) -> BigInt:
    if x.radix != y.radix:
        raise ValueError("Numbers must use same radix")
    if x.negative == y.negative:
        words = []
        carry = 0
        for i in range(max(len(x.words), len(y.words))):
            x_digit = x.words[i] if i < len(x.words) else 0
            y_digit = y.words[i] if i < len(y.words) else 0
            carry, digit = divmod(x_digit + y_digit + carry, x.radix)
            words.append(digit)
        if carry:
            words.append(carry)
        return BigInt(words, x.radix, x.negative)
    
    comparison = x.compare_magnitude(y)
    if comparison == 0:
        return BigInt([0], x.radix)
    if comparison > 0:
        return BigInt(subtract_magnitudes(x, y), x.radix, x.negative)
    return BigInt(subtract_magnitudes(y, x), x.radix, y.negative)