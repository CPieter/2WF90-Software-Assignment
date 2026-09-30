from src.integer.BigInt import BigInt

def divmod_bigint(x: BigInt, y: BigInt) -> tuple[BigInt, BigInt]:
    radix = x.radix
    x_abs = abs(x)
    y_abs = abs(y)

    if y.is_zero():
        raise ZeroDivisionError()

    if x_abs < y_abs:
        q, r = BigInt([0], radix), x_abs
    else:
        split = len(x.words) - len(y.words) + 1
        r = BigInt(x.words[split:] or [0], radix)

        q = []
        for digit in reversed(x.words[:split]):
            r = BigInt([digit] + r.words, radix)
            count = 0
            while r >= y:
                r = r - y
                count += 1
            q.append(count)
        q = BigInt(list(reversed(q)), radix)

    if x.negative and not r.is_zero():
        q = q + BigInt([1], radix)
        r = y_abs - r
    if x.negative != y.negative:
        q = -q
    return q, r