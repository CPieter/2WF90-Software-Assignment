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

from polynomial.Polynomial import Polynomial
from polynomial.addition import add as polynomial_add
from polynomial.subtraction import subtract as polynomial_subtract
from finite_field.addition import add as field_add
from finite_field.subtraction import subtract as field_subtract


def solve(exercise: dict) -> dict:
    task = exercise["task"]

    f = Polynomial(exercise["f"]) if "f" in exercise else None
    g = Polynomial(exercise["g"]) if "g" in exercise else None

    int_mod = exercise["integer_modulus"]
    pol_mod = Polynomial(exercise["polynomial_modulus"]) if "polynomial_modulus" in exercise else None
    degree = exercise["degree"] if "degree" in exercise else None

    result = None

    if exercise["type"] == "polynomial_arithmetic":
        if task == "addition":
            result = polynomial_add(f, g, int_mod)
        elif task == "subtraction":
            result = polynomial_subtract(f, g, int_mod)
        elif task == "multiplication":
            pass
        elif task == "long_division":
            pass
        elif task == "extended_euclidean_algorithm":
            pass
        elif task == "irreducibility_check":
            pass
        elif task == "irreducible_element_generation":
            pass

    elif exercise["type"] == "finite_field_arithmetic":
        if task == "addition":
            result = field_add(f, g, int_mod, pol_mod)
        elif task == "subtraction":
            result = field_subtract(f, g, int_mod, pol_mod)
        elif task == "multiplication":
            pass
        elif task == "division":
            pass
        elif task == "primitivity_check":
            pass
        elif task == "primitive_element_generation":
            pass

    answer = {
        "answer": result.coeffs,
    }

    return answer

def solve_exercise(exercise_location: str, answer_location: str) -> None:
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    answer = solve(exercise)

    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)