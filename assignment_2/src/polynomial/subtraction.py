from polynomial.Polynomial import Polynomial

def subtract(f: Polynomial, g: Polynomial) -> Polynomial:
    if f.int_mod != g.int_mod:
        raise ValueError("Cannot subtract polynomials with different moduli")
    return f + -g
