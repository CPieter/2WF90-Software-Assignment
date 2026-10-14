##
# 2WF90 Algebra for Security -- Software Assignment 1 
# Integer and Modular Arithmetic
# solve.py
#
#
# Group number:
# 1
#
# Author names and student IDs:
# Juan José Mejía Trejos (2009404)
# Ivan Dimitrov (2282526)
# Quinn Grosse (2361175)
# Pieter Conderaerts (1854208)
##

import json

from finite_field.division import divide
from finite_field.inversion import invert
from polynomial.Polynomial import Polynomial
from polynomial.addition import add as polynomial_add
from polynomial.extended_euclidean_algorithm import extended_euclidean_algorithm
from polynomial.long_division import long_divide
from polynomial.subtraction import subtract as polynomial_subtract
from polynomial.multiplication import multiply as polynomial_mult
from finite_field.addition import add as field_add
from finite_field.subtraction import subtract as field_subtract
from finite_field.multiplication import multiply as field_multiply


def solve(exercise: dict) -> dict:
    task = exercise["task"]

    int_mod = exercise["integer_modulus"]
    pol_mod = Polynomial(exercise["polynomial_modulus"], int_mod) if "polynomial_modulus" in exercise else None
    degree = exercise["degree"] if "degree" in exercise else None

    f = Polynomial(exercise["f"], int_mod) if "f" in exercise else None
    g = Polynomial(exercise["g"], int_mod) if "g" in exercise else None

    if exercise["type"] == "polynomial_arithmetic":
        if task == "addition":
            return {"answer": polynomial_add(f, g).coeffs}
        elif task == "subtraction":
            return {"answer": polynomial_subtract(f, g).coeffs}
        elif task == "multiplication":
            return {"answer": polynomial_mult(f, g).coeffs}
        elif task == "long_division":
            if g.is_zero():
                return {"answer-q": None, "answer-r": None}
            q, r = long_divide(f, g)
            return {"answer-q": q.coeffs, "answer-r": r.coeffs}
        elif task == "extended_euclidean_algorithm":
            if f.is_zero() and g.is_zero():
                return {"answer-a": None, "answer-b": None, "answer-gcd": None}
            a, b, gcd = extended_euclidean_algorithm(f, g)
            return {"answer-a": a.coeffs, "answer-b": b.coeffs, "answer-gcd": gcd.coeffs}
        elif task == "irreducibility_check":
            pass
        elif task == "irreducible_element_generation":
            pass

    elif exercise["type"] == "finite_field_arithmetic":
        if task == "addition":
            return {"answer": field_add(f, g, pol_mod).coeffs}
        elif task == "subtraction":
            return {"answer": field_subtract(f, g, pol_mod).coeffs}
        elif task == "multiplication":
            return {"answer": field_multiply(f, g, pol_mod).coeffs}
        elif task == "division":
            if g.is_zero():
                return {"answer": None}
            return {"answer": divide(f, g, pol_mod).coeffs}
        elif task == "inversion":
            if f.is_zero():
                return {"answer": None}
            return {"answer": invert(f, pol_mod).coeffs}
        elif task == "primitivity_check":
            pass
        elif task == "primitive_element_generation":
            pass

    return NotImplemented

def solve_exercise(exercise_location: str, answer_location: str) -> None:
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    answer = solve(exercise)

    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)
