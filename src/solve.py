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

from src.integer import multiplication_primary
from src.integer.BigInt import BigInt
from src.integer.addition import add
from src.integer.extended_euclidian_algorithm import extended_euclid
from src.integer.multiplication_karatsuba import multiply_karatsuba
from src.integer.multiplication_primary import multiply_primary
from src.integer.subtraction import subtract
from src.modular.reduction import reduction
from src.modular.inversion import inversion

def solve(exercise: dict) -> dict:
    radix = exercise["radix"]
    operation = exercise["operation"]

    x = BigInt.from_string(exercise["x"], radix)
    y = BigInt.from_string(exercise["y"], radix) if "y" in exercise else None
    modulus = (
        BigInt.from_string(exercise["modulus"], radix)
        if "modulus" in exercise
        else None
    )

    result = None

    if exercise["type"] == "integer_arithmetic":
        if operation == "addition":
            result = add(x, y)
        elif operation == "subtraction":
            result = subtract(x, y)
        elif operation == "multiplication_primary":
            result = multiply_primary(x, y)
        elif operation == "extended_euclidean_algorithm":
            result = extended_euclid(x, y)
        elif operation == "multiplication_karatsuba":
            result = multiply_karatsuba(x, y)

    elif exercise["type"] == "modular_arithmetic":
        if operation == "reduction":
            result = reduction(x, modulus)
        elif operation == "inversion":
            result = inversion(x, modulus)
        elif operation == "addition":
            result = reduction(add(x, y), modulus)
        elif operation == "subtraction":
            result = reduction(subtract(x, y), modulus)
        elif operation == "multiplication":
            result = reduction(multiply_primary(x, y), modulus)

    if operation == "extended_euclidean_algorithm":
        if result is None:
            return {"answer-a": None, "answer-b": None, "answer-gcd": None}
        a, b, gcd = result
        return {
            "answer-a": a.to_string(),
            "answer-b": b.to_string(),
            "answer-gcd": gcd.to_string(),
        }

    return {"answer": None if result is None else result.to_string()}

def solve_exercise(exercise_location: str, answer_location: str) -> None:
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    answer = solve(exercise)

    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)

if __name__ == '__main__':
    solve_exercise('data/Simple/Exercises/exercise0.json', 'output.json')
