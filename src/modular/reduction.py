from integer.BigInt import BigInt

def reduction(x: BigInt, modulus: BigInt) -> BigInt | None:
    radix = x.radix
    m = BigInt(modulus.words, radix)
    r = BigInt(x.words, radix)
    if modulus.is_zero():
        return None

    k = len(r.words)
    n = len(m.words)

    for i in range(k-n, -1, -1):
        shifted = BigInt([0] * i + m.words, radix)
        while r.compare_magnitude(shifted) >= 0:
            r = r - shifted

    if x.negative and not r.is_zero():
        r = m - r

    return r
