from polynomial.Polynomial import Polynomial

def extended_euclidean_algorithm(a: Polynomial, b: Polynomial) -> tuple[Polynomial, Polynomial, Polynomial]:
    if a.int_mod != b.int_mod:
        raise ValueError("Cannot perform extended euclidean algorithm on polynomials with different moduli")

    int_mod = a.int_mod

    x = Polynomial([1], int_mod)
    y = Polynomial([0], int_mod)
    u = Polynomial([0], int_mod)
    v = Polynomial([1], int_mod)

    while not b.is_zero():
        q, r = divmod(a, b)
        a = b
        b = r
        x_p = x
        y_p = y
        x = u
        y = v
        u = x_p - q * u
        v = y_p - q * v

    c = Polynomial([pow(a.lc(), -1, int_mod)], int_mod)
    return x*c, y*c, a*c