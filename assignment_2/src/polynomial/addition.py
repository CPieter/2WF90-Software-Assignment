from polynomial.Polynomial import Polynomial


def add(f: Polynomial, g: Polynomial, int_mod: int) -> Polynomial:
    if int_mod < 2:
        raise ValueError("The modulus must be greater than 1")
    n = max(len(f.coeffs), len(g.coeffs))
    coeffs = [0] * n

    for i in range(n):
        a = f.coeffs[i] if i < len(f.coeffs) else 0
        b = g.coeffs[i] if i < len(g.coeffs) else 0
        coeffs[i] = (a + b) % int_mod

    return Polynomial(coeffs)