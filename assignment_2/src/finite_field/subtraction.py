from polynomial.Polynomial import Polynomial
from polynomial.subtraction import subtract as polynomial_subtract
from finite_field.reduction import reduce_in_field

def subtract(f: Polynomial, g: Polynomial, int_mod: int, poly_mod: Polynomial) -> Polynomial:
    result = polynomial_subtract(f, g, int_mod)
    return reduce_in_field(result, int_mod, poly_mod)