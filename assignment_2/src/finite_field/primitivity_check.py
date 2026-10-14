from polynomial.Polynomial import Polynomial

def prime_divisors(n: int) -> list[int]:
    f = set()
    x = 2

    while x * x <= n:
        if n % x == 0:
            f.add(x)
            n = n // x
        x += 1
    if n > 1:
        f.add(x)
    return sorted(list(f))

def is_primitive(a: Polynomial, h: Polynomial) -> bool:
    if a.is_zero():
        return False
    q = h.int_mod ** h.degree()
    p = prime_divisors(q -1)
    k = len(p)
    i = 0

    while i < k and pow(a, (q - 1) // p[i], h) != Polynomial([1], h.int_mod):
        i = i + 1
    return i == k


