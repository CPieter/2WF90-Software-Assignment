from polynomial.Polynomial import Polynomial
from polynomial.extended_euclidean_algorithm import extended_euclidean_algorithm


def invert(f: Polynomial, h: Polynomial) -> Polynomial:
    if f.is_zero():
        raise ZeroDivisionError("Zero has no inverse")
    x, _, _ = extended_euclidean_algorithm(f, h)
    return x % h