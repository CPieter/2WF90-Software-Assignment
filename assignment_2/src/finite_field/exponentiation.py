from finite_field.multiplication import multiply
from polynomial.Polynomial import Polynomial

def bin_exp(x: Polynomial, a: int, h: Polynomial) -> Polynomial:

    z = Polynomial([1], x.p)
    x = x % h

    for a_i in bin(a)[2:]:
        z = multiply(z, z, h)
        if a_i == "1":
            z = multiply(x, z, h)
    return z