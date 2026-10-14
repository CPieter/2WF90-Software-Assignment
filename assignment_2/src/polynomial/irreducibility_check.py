from polynomial.Polynomial import Polynomial
from polynomial.extended_euclidean_algorithm import extended_euclidean_algorithm


def gcd(f: Polynomial, g: Polynomial) -> Polynomial:
    _, _, gcdiv = extended_euclidean_algorithm(f, g)
    return gcdiv

def is_irreducible(f: Polynomial) -> bool:
    X = Polynomial([0, 1], f.p)

    t = 1
    while gcd(f, pow(X, f.p**t, f) - X) == Polynomial([1], f.p):
        t = t + 1
    return t == f.degree()