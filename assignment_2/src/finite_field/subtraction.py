from polynomial.Polynomial import Polynomial
from polynomial.subtraction import subtract as polynomial_subtract

def subtract(f: Polynomial, g: Polynomial, h: Polynomial) -> Polynomial:
    return (f - g) % h