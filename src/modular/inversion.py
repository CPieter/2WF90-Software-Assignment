from src.integer.BigInt import BigInt
from src.modular.reduction import reduction

def inversion(x: BigInt, modulus: BigInt) -> BigInt | None:
    if x.radix != modulus.radix:
        raise ValueError("Radices must match")
    if modulus.is_zero():
        return None
    radix = x.radix
    m = BigInt(modulus.words, radix)
    one = BigInt([1], radix)
    old_r = m
    r = reduction(x, m)
    old_t = BigInt([0], radix)
    t = one
    
    while not r.is_zero():
        remainder = old_r
        coefficient = old_t
        for i in range(len(old_r.words) - len(r.words), -1, -1):
            shifted_r = BigInt([0] * i + r.words, radix)
            shifted_t = BigInt([0] * i + t.words, radix, t.negative)
            
            while remainder.compare_magnitude(shifted_r) >= 0:
                remainder = remainder - shifted_r
                coefficient = coefficient - shifted_t
                
        old_r, r = r, remainder
        old_t, t = t, coefficient
        
    # If the GCD is not 1, then the inverse does not exist
    if old_r.compare_magnitude(one) != 0:
        return None
    return reduction(old_t, m)