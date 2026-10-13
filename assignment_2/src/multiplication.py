from polynomial.Polynomial import Polynomial

def mult(f: Polynomial, g: Polynomial, int_mod: int) -> Polynomial:
    n = len(f.coeffs)-1
    m = len(g.coeffs)-1
    mult_poly = [0] * (n+m+1)

    for i in range(n+m+1):
        coeff_i = 0
        for j in range(i):
            if i <= n and (i-j) <= m:
                coeff_i += f.coeffs[i]*g.coeffs[i-j]
        mult_poly[i] = coeff_i % int_mod

    return Polynomial(mult_poly)
