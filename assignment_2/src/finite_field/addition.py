from polynomial.Polynomial import Polynomial
from polynomial.addition import add as polynomial_add 

def add(f: Polynomial, g: Polynomial, h: Polynomial) -> Polynomial:
    return (f + g) % h