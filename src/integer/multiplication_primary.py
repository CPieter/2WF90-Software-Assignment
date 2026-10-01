from src.integer.BigInt import BigInt

def multiply_primary(x: BigInt, y: BigInt) -> BigInt:
    if x.radix != y.radix:
        raise ValueError("Numbers must use same radix")

    if x.is_zero() or y.is_zero():
        return BigInt([0], radix=x.radix)

    radix = x.radix
    z = [0] * (len(x.words) + len(y.words))

    for i, xd in enumerate(x.words):
        c = 0
        for j, yd in enumerate(y.words):
            t = z[i + j] + x.words[i] * y.words[j] + c
            c = t // radix
            z[i+j] = t - c * radix
        z[i + len(y.words)] += c

    return BigInt(z, radix, x.negative != y.negative)