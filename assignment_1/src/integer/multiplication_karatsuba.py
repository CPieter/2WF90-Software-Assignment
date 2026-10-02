from integer.BigInt import BigInt
from integer.multiplication_primary import multiply_primary


def multiply_karatsuba(x: BigInt, y: BigInt) -> BigInt:
    if x.radix != y.radix:
        raise ValueError("Numbers must use same radix")

    if len(x.words) <= 1 or len(y.words) <= 1:
        return multiply_primary(x, y)

    negative = x.negative != y.negative
    x = abs(x)
    y = abs(y)

    m = max(len(x.words), len(y.words)) // 2
    x0, x1 = x.split(m)
    y0, y1 = y.split(m)

    z0 = multiply_karatsuba(x0, y0)
    z2 = multiply_karatsuba(x1, y1)
    z1 = multiply_karatsuba(x0 + x1, y0 + y1) - z2 - z0

    z = z2.shift(2*m) + z1.shift(m) + z0
    return -z if negative else z