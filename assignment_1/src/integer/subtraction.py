from integer.BigInt import BigInt

def subtract_magnitudes(larger: BigInt, smaller: BigInt) -> list[int]:
    if larger.compare_magnitude(smaller) < 0:
        raise ValueError("First magnitude must be at least the same as the second one")
    words = []
    borrow = 0
    for i in range(len(larger.words)):
        other_digit = smaller.words[i] if i < len(smaller.words) else 0
        digit = larger.words[i] - other_digit - borrow 
        if digit < 0:
            digit += larger.radix
            borrow = 1
        else:
            borrow = 0
        words.append(digit)
    return words

def subtract(x: BigInt, y: BigInt) -> BigInt:
    """To re-use addition subtraction will be used as x + (-y) instead of x - y""" 
    from integer.addition import add
    return add(x, -y)