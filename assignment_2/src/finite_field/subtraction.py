from polynomial.Polynomial import Polynomial
from polynomial.subtraction import subtract as polynomial_subtract

def subtract(f: Polynomial, g: Polynomial, poly_mod: Polynomial) -> Polynomial:
    return polynomial_subtract(f, g)