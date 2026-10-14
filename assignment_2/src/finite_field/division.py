from finite_field.inversion import invert
from finite_field.multiplication import multiply
from polynomial.Polynomial import Polynomial

def divide(f: Polynomial, g: Polynomial, h: Polynomial) -> Polynomial:
    return multiply(f, invert(g, h), h)