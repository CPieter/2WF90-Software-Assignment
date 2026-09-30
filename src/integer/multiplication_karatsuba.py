from src.integer.BigInt import BigInt
from src.integer.multiplication_primary import multiply_primary


def multiply_karatsuba(x: BigInt, y: BigInt) -> BigInt:
    if x.radix != y.radix:
        raise ValueError("Numbers must use same radix")

    if len(x.words) <= 1 or len(y.words) <= 1:
        return multiply_primary(x, y)

    negative = x.negative != y.negative
    x = abs(x)
    y = abs(y)

    m = max(len(x.words), len(y.words)) // 2
    x0, x1 = split(x, m)
    y0, y1 = split(y, m)

    z0 = multiply_karatsuba(x0, y0)
    z2 = multiply_karatsuba(x1, y1)
    z1 = multiply_karatsuba(x0 + x1, y0 + y1) - z2 - z0

    z = shift(z2, 2 * m) + shift(z1, m) + z0
    return -z if negative else z


def split(x: BigInt, m: int) -> tuple[BigInt, BigInt]:
    low = x.words[:m] or [0]
    high = x.words[m:] or [0]
    return BigInt(low, x.radix), BigInt(high, x.radix)


def shift(x: BigInt, k: int) -> BigInt:
    if x.is_zero() or k == 0:
        return x
    return BigInt([0] * k + x.words, x.radix, x.negative)
