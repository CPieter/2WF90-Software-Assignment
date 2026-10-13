from polynomial.Polynomial import Polynomial

def multiply(f: Polynomial, g: Polynomial) -> Polynomial:
    if f.int_mod != g.int_mod:
        raise ValueError("Cannot multiply polynomials with different moduli")

    int_mod = f.int_mod
    n = len(f.coeffs)-1
    m = len(g.coeffs)-1
    mult_poly = [0] * (n+m+1)

    for i in range(n+m+1):
        coeff_i = 0
        for j in range(i+1):
            if j <= n and (i-j) <= m:
                coeff_i += f.coeffs[j]*g.coeffs[i-j]
        mult_poly[i] = coeff_i % int_mod

    return Polynomial(mult_poly, int_mod)
