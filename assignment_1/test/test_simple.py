import json
import sys
import unittest
from pathlib import Path

ASSIGNMENT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ASSIGNMENT_DIR / "src"))

from solve import solve

DATA_DIR = ASSIGNMENT_DIR / "data" / "Simple"


class TestSimple(unittest.TestCase):

    def _test_simple(self, num: int):
        with open(DATA_DIR / "Exercises" / f"exercise{num}.json", "r") as exercise_file:
            exercise = json.load(exercise_file)

        actual = solve(exercise)

        with open(DATA_DIR / "Answers" / f"answer{num}.json", "r") as answer_file:
            expected = json.load(answer_file)

        self.assertEqual(expected, actual)

    def test_simple00(self):
        self._test_simple(0)

    def test_simple01(self):
        self._test_simple(1)

    def test_simple02(self):
        self._test_simple(2)

    def test_simple03(self):
        self._test_simple(3)

    def test_simple04(self):
        self._test_simple(4)

    def test_simple05(self):
        self._test_simple(5)

    def test_simple06(self):
        self._test_simple(6)

    def test_simple07(self):
        self._test_simple(7)

    def test_simple08(self):
        self._test_simple(8)

    def test_simple09(self):
        self._test_simple(9)

    def test_simple10(self):
        self._test_simple(10)

    def test_simple11(self):
        self._test_simple(11)

    def test_simple12(self):
        self._test_simple(12)

    def test_simple13(self):
        self._test_simple(13)

if __name__ == "__main__":
    unittest.main()