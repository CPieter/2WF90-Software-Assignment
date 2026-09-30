from src.integer.BigInt import BigInt

def multiply_primary(x: BigInt, y: BigInt) -> BigInt:
    if x.radix != y.radix:
        raise ValueError("Numbers must use same radix")

    if x.is_zero() or y.is_zero():
        return BigInt([0], radix=x.radix)

    radix = x.radix
    negative = x.negative != y.negative
    words = [0] * (len(x.words) + len(y.words))

    for i, xd in enumerate(x.words):
        carry = 0
        for j, yd in enumerate(y.words):
            total = words[i + j] + xd * yd + carry
            words[i + j] = total % radix
            carry = total // radix
        words[i + len(y.words)] += carry

    return BigInt(words, radix, negative)