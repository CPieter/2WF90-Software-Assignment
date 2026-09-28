##
# 2WF90 Algebra for Security -- Software Assignment 1 
# Integer and Modular Arithmetic
# solve.py
#
#
# Group number:
# group_number 
#
# Author names and student IDs:
# author_name_1 (author_student_ID_1) 
# author_name_2 (author_student_ID_2)
# author_name_3 (author_student_ID_3)
# author_name_4 (author_student_ID_4)
##

# Import built-in json library for handling input/output 
import json
from src.integer.BigInt import BigInt
from src.integer.addition import add
from src.integer.subtraction import subtract

def solve_exercise(exercise_location : str, answer_location : str):
    """
    solves an exercise specified in the file located at exercise_location and
    writes the answer to a file at answer_location. Note: the file at
    answer_location might not exist yet and, hence, might still need to be created.
    """
    
    # Open file at exercise_location for reading.
    with open(exercise_location, "r") as exercise_file:
        # Deserialize JSON exercise data present in exercise_file to corresponding Python exercise data 
        exercise = json.load(exercise_file)
        

    ### Parse and solve ###
    radix = exercise["radix"]
    operation = exercise["operation"]
    x = BigInt.from_string(exercise["x"], radix)
    y = BigInt.from_string(exercise["y"], radix) if "y" in exercise else None
    modulus = (BigInt.from_string(exercise["modulus"], radix)
               if "modulus" in exercise else None)
    result = None

    # Check type of exercise
    if exercise["type"] == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to solve
        if exercise["operation"] == "addition":
            # Solve integer arithmetic addition exercise
            result = add(x, y)
        elif exercise["operation"] == "subtraction":
            # Solve integer arithmetic subtraction exercise
            result = subtract(x, y)
        elif exercise["operation"] == "multiplication_primary":
            # Solve integer arithmetic multiplication exercise using the primary school method
            pass
        elif exercise["operation"] == "extended_euclidean_algorithm":
            # Perform the extended Euclidean algorithm
            pass
        elif exercise["operation"] == "multiplication_karatsuba":
            # Solve integer arithmetic multiplication exercise using the Karatsuba method
            pass
    else: # exercise["type"] == "modular_arithmetic"
        # Check what operation within the modular arithmetic operations we need to solve
        if exercise["operation"] == "reduction":
            # Solve modular arithmetic reduction exercise
            pass
        elif exercise["operation"] == "inversion":
            # Solve modular arithmetic inversion exercise
            pass
        elif exercise["operation"] == "addition":
            # Solve modular arithmetic addition exercise
            pass
        elif exercise["operation"] == "subtraction":
            # Solve modular arithmetic subtraction exercise
            pass
        elif exercise["operation"] == "multiplication":
            # Solve modular arithmetic multiplication exercise
            pass

    if operation == "extended_euclidean_algorithm":
        if result is None:
            answer = {"answer-a": None, "answer-b": None, "answer-gcd": None}
        else:
            a, b, gcd = result 
            answer = {"answer-a": a.to_string(),
                      "answer-b": b.to_string(),
                      "answer-gcd": gcd.to_string()}
    else:
        answer = {"answer": None if result is None else result.to_string()}

    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)

if __name__ == '__main__':
    solve_exercise('data/Simple/Exercises/exercise0.json', 'output.json')