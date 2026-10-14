from finite_field.primitivity_check import is_primitive
from polynomial.Polynomial import Polynomial

def generate_primitive_element(h: Polynomial) -> Polynomial:
    a = Polynomial.random_residue(h)
    while not is_primitive(a, h):
        a = Polynomial.random_residue(h)
    return a