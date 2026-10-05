from polynomial.Polynomial import Polynomial

def reduce_in_field(
    f: Polynomial,
    int_mod: int,
    poly_mod: Polynomial
) -> Polynomial:
    if int_mod < 2:
        raise ValueError("The coefficient modulus must be greater than 1")
    remainder = Polynomial([c % int_mod for c in f.coeffs] or [0]).coeffs
    modulus = Polynomial([c % int_mod for c in poly_mod.coeffs] or [0])
    if modulus.degree() < 1:
        raise ValueError("The polynomial modulus must have a positive degree")
    inverse_leading = pow(modulus.coeffs[-1], int_mod - 2, int_mod)
    while remainder != [0] and len(remainder) >= len(modulus.coeffs):
        shift = len(remainder) - len(modulus.coeffs)
        factor = (remainder[-1] * inverse_leading) % int_mod
        for i in range(len(modulus.coeffs)):
            position = i + shift
            remainder[position] = (remainder[position] - factor * modulus.coeffs[i]) % int_mod
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return Polynomial(remainder)