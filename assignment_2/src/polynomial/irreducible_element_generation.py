from polynomial.Polynomial import Polynomial
from polynomial.irreducibility_check import is_irreducible

def generate_irreducible_element(deg: int, p: int) -> Polynomial:
    f = Polynomial.random_of_degree(deg, p)
    while not is_irreducible(f):
        f = Polynomial.random_of_degree(deg, p)
    return f