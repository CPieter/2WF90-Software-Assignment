from src.integer.BigInt import BigInt
from src.modular.reduction import reduction

def inversion(x: BigInt, modulus: BigInt) -> BigInt | None:
    if x.radix != modulus.radix:
        raise ValueError("Radices must match")
    if modulus.is_zero():
        return None
    radix = x.radix
    m = BigInt(modulus.words, radix)
    one = BigInt([1], radix)

    old_r = m
    r = reduction(x, m)
    old_t = BigInt([0], radix)
    t = one

    while not r.is_zero():
        q, rem = divmod(old_r, r)
        old_r, r = r, rem
        old_t, t = t, old_t - q * t

    if old_r.compare_magnitude(one) != 0:
        return None
    return reduction(old_t, m)