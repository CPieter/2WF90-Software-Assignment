from src.integer.BigInt import BigInt

def multiplication(x: BigInt, y: BigInt) -> BigInt:
    radix = x.radix

    m = len(x.words)
    n = len(y.words)

    z = [0] * (m+n)

    for i in range(m):
        c = 0
        for j in range(n):
            t = z[i+j]+(x.words[i]*y.words[j])+c
            c = t // radix
            z[i+j]= t-(c*radix)
        z[i+n] = c

    return BigInt(z, radix)

