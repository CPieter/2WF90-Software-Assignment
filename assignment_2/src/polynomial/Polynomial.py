
class Polynomial:
    def __init__(self, coeffs: list[int]):
        self.coeffs = coeffs.copy()
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()

    def is_zero(self) -> bool:
        return self.coeffs == [0]

    def degree(self) -> int:
        return -1 if self.is_zero() else len(self.coeffs) - 1