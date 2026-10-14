from polynomial.Polynomial import Polynomial
from polynomial.extended_euclidean_algorithm import extended_euclidean_algorithm


def invert(f: Polynomial, h: Polynomial) -> Polynomial:
    x, _, gcd = extended_euclidean_algorithm(f, h)
    if gcd != Polynomial([1], h.p):
        raise ZeroDivisionError("f is not invertible modulo h")
    return x % h