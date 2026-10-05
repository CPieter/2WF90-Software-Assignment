from polynomial.Polynomial import Polynomial
from polynomial.addition import add

def subtract(f: Polynomial, g: Polynomial, int_mod: int) -> Polynomial:
    negative_g = Polynomial([-coefficient for coefficient in g.coeffs])
    return add(f, negative_g, int_mod)
