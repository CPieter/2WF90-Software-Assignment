from polynomial.Polynomial import Polynomial
from polynomial.extended_euclidean_algorithm import extended_euclidean_algorithm


def invert(f: Polynomial, h: Polynomial) -> Polynomial:
    if f.is_zero():
        raise ZeroDivisionError("Zero has no inverse")
    x, _, gcd = extended_euclidean_algorithm(f, h)
    if gcd != Polynomial([1], h.int_mod):
        raise ZeroDivisionError("f is not invertible modulo h")
    return x % h