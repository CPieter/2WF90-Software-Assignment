from src.integer.BigInt import BigInt

def multiply_primary(x: BigInt, y: BigInt) -> BigInt:
    if x.radix != y.radix:
        raise ValueError("Numbers must use same radix")

    if x.is_zero() or y.is_zero():
        return BigInt([0], radix=x.radix)

    radix = x.radix
    negative = x.negative != y.negative

    result = BigInt([0] * (len(x.words) + len(y.words)), radix, negative)

    for i in range(len(x.words)):
        carry = 0

        for j in range(len(y.words)):
            total = result.words[i + j] + x.words[i] * y.words[j] + carry
            result.words[i + j] = total % radix
            carry = total // radix

        result.words[i + len(y.words)] += carry

    return result