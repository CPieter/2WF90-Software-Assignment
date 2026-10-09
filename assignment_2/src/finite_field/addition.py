from polynomial.Polynomial import Polynomial
from polynomial.addition import add as polynomial_add 

def add(f: Polynomial, g: Polynomial, int_mod: int, poly_mod: Polynomial) -> Polynomial:
    return polynomial_add(f, g, int_mod)