from polynomial.Polynomial import Polynomial

def long_divide(a: Polynomial, b: Polynomial) -> tuple[Polynomial, Polynomial]:
    if b.is_zero():
        raise ZeroDivisionError("Division by the zero polynomial")

    int_mod = a.p
    q = Polynomial([0], int_mod)
    r = a.copy()

    inv = pow(b.lc(), -1, int_mod)
    while r.degree() >= b.degree():
        term = Polynomial([r.lc() * inv], int_mod).shift(r.degree() - b.degree())
        q = q + term
        r = r - term * b
    return q, r