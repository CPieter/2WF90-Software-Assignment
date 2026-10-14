from polynomial.Polynomial import Polynomial

def extended_euclidean_algorithm(a: Polynomial, b: Polynomial) -> tuple[Polynomial, Polynomial, Polynomial]:
    if a.is_zero() and b.is_zero():
        raise ZeroDivisionError("gcd(0, 0) is undefined")

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

    c = pow(a.lc(), -1, int_mod)
    return x*c, y*c, a*c