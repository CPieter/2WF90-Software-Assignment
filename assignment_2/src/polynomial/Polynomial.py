from random import randint


class Polynomial:
    def __init__(self, coeffs: list[int], int_mod: int):
        if int_mod < 2:
            raise ValueError("The modulus must be greater than 1")
        self.p = int_mod
        self.coeffs = [c % int_mod for c in coeffs]
        if not self.coeffs:
            self.coeffs = [0]
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()

    @classmethod
    def random_of_degree(cls, deg: int, p: int):
        coeffs = [randint(0, p - 1) for _ in range(deg)]
        coeffs.append(randint(1, p - 1))
        return cls(coeffs, p)

    @classmethod
    def random_residue(cls, h: "Polynomial") -> "Polynomial":
        return cls([randint(0, h.p - 1) for _ in range(h.degree())], h.p)

    def is_zero(self) -> bool:
        return self.coeffs == [0]

    def degree(self) -> int:
        return -1 if self.is_zero() else len(self.coeffs) - 1

    def lc(self) -> int:
        return self.coefficient(self.degree())
    
    def coefficient(self, i: int) -> int:
        if i < 0:
            raise ValueError("Degree must be non-negative")
        if i >= len(self.coeffs):
            return 0
        return self.coeffs[i]
    
    def copy(self) -> "Polynomial":
        return Polynomial(self.coeffs, self.p)
    
    def shift(self, k: int) -> "Polynomial":
        if k < 0:
            raise ValueError("Shift must be non-negative")
        if self.is_zero() or k == 0:
            return self.copy()
        return Polynomial([0] * k + self.coeffs, self.p)
       
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Polynomial):
            return False
        return self.coeffs == other.coeffs and self.p == other.p

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        from polynomial.addition import add
        return add(self, other)

    def __neg__(self):
        return Polynomial([-c for c in self.coeffs], self.p)

    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        from polynomial.subtraction import subtract
        return subtract(self, other)

    def __mul__(self, other):
        if isinstance(other, int):
            return Polynomial([(c * other) % self.p for c in self.coeffs], self.p)
        if not isinstance(other, Polynomial):
            return NotImplemented
        from polynomial.multiplication import multiply
        return multiply(self, other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __divmod__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        from polynomial.long_division import long_divide
        return long_divide(self, other)

    def __floordiv__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        return divmod(self, other)[0]

    def __mod__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        return divmod(self, other)[1]

    def __pow__(self, power, modulo=None):
        if not isinstance(power, int):
            return NotImplemented
        if power < 0:
            raise ValueError("Exponent must be non-negative")
        if modulo is None:
            raise ValueError("Use pow(x, a, h): a modulus polynomial is required")
        if not isinstance(modulo, Polynomial):
            return NotImplemented
        from finite_field.exponentiation import bin_exp
        return bin_exp(self, power, modulo)