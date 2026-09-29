import json

def compare_answer(output_path, answer_path):
    with open(output_path, "r") as f:
        out = json.load(f)
        if "answer" in out:
            output = out["answer"]
            output_a = None
            output_b = None
            output_gcd = None
        else:
            output = None
            output_a = out["answer-a"]
            output_b = out["answer-b"]
            output_gcd = out["answer-gcd"]

    with open(answer_path, "r") as f:
        ans = json.load(f)
        if "answer" in ans:
            answer = ans["answer"]
            answer_a = None
            answer_b = None
            answer_gcd = None
        else:
            answer = None
            answer_a = ans["answer-a"]
            answer_b = ans["answer-b"]
            answer_gcds = ans["answer-gcd"]

    if output == answer and output_a == answer_a and output_b == answer_b and output_gcd == answer_gcd:
        return ("Correct")
    else :
        return ("Incorrect")