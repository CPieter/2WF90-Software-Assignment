from integer.BigInt import BigInt


def extended_euclid(x: BigInt, y: BigInt) -> tuple[BigInt, BigInt, BigInt]:
    zero, one = BigInt([0], x.radix), BigInt([1], x.radix)
    old_r, r = abs(x), abs(y)
    old_s, s = one, zero
    old_t, t = zero, one

    while not r.is_zero():
        q, rem = divmod(old_r, r)
        old_r, r = r, rem
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    a = -old_s if x.negative else old_s
    b = -old_t if y.negative else old_t
    return a, b, old_r