
class Polynomial:
    def __init__(self, coeffs: list[int]):
        self.coeffs = coeffs.copy()
        if not self.coeffs:
            self.coeffs = [0]
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()

    def is_zero(self) -> bool:
        return self.coeffs == [0]

    def degree(self) -> int:
        return -1 if self.is_zero() else len(self.coeffs) - 1
    
    def coefficient(self, i: int) -> int:
        if i < 0:
            raise ValueError("Degree must be non-negative")
        if i >= len(self.coeffs):
            return 0
        return self.coeffs[i]
    
    def reduce_coefficients(self, p : int) -> "Polynomial":
        if p < 2:
            raise ValueError("The modulus must be greater than 1")
        reduced = [coefficient % p for coefficient in self.coeffs]
        return Polynomial(reduced)
    
    def copy(self) -> "Polynomial":
        return Polynomial(self.coeffs)
    
    def shift(self, k: int) -> "Polynomial":
        if k < 0:
            raise ValueError("Shift must be non-negative")
        if self.is_zero() or k == 0:
            return self.copy()
        return Polynomial([0] * k + self.coeffs)
    
    def split(self, m: int) -> tuple["Polynomial", "Polynomial"]:
        if m < 0:
            raise ValueError("Split position must be non-negative")
        return (
            Polynomial(self.coeffs[:m]),
            Polynomial(self.coeffs[m:])
        )
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Polynomial):
            return False
        return self.coeffs == other.coeffs