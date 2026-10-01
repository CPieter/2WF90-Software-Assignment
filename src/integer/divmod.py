from src.integer.BigInt import BigInt

def divmod_bigint(x: BigInt, y: BigInt) -> tuple[BigInt, BigInt]:
    if y.is_zero():
        raise ZeroDivisionError("division by zero")

    radix = x.radix
    y_abs = abs(y)

    k = max(len(x.words) - len(y_abs.words) + 1, 0)
    _, r = x.split(k)
    q_digits = []
    for digit in reversed(x.words[:k]):
        r = r.shift(1) + BigInt([digit], radix)
        count = 0
        while r >= y_abs:
            r = r - y_abs
            count += 1
        q_digits.append(count)
    q = BigInt(q_digits[::-1] or [0], radix)

    if x.negative != y.negative:
        if not r.is_zero():
            q = q + BigInt([1], radix)
            r = y_abs - r
        q = -q
    if y.negative:
        r = -r

    return q, r