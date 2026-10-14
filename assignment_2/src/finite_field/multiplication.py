from polynomial.Polynomial import Polynomial

def multiply(f: Polynomial, g: Polynomial, h: Polynomial) -> Polynomial:
    return (f * g) % h