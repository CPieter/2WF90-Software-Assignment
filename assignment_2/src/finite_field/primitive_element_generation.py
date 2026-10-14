from random import randint

from finite_field.primitivity_check import is_primitive
from polynomial.Polynomial import Polynomial

def random_polynomial(h: Polynomial):
    return Polynomial([randint(0, h.int_mod) for _ in range(h.degree())], h.int_mod)

def generate_primitive_element(h: Polynomial) -> Polynomial:
    a = random_polynomial(h)
    while not is_primitive(a, h):
        a = random_polynomial(h)
    return a