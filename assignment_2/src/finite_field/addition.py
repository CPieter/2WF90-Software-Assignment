from polynomial.Polynomial import Polynomial
from polynomial.addition import add as polynomial_add 
from finite_field.reduction import reduce_in_field

def add(f: Polynomial, g: Polynomial, int_mod: int, poly_mod: Polynomial) -> Polynomial:
    result = polynomial_add(f, g, int_mod)
    return reduce_in_field(result, int_mod, poly_mod)