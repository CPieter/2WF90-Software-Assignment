import json
import sys
import unittest
from pathlib import Path

ASSIGNMENT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ASSIGNMENT_DIR / "src"))

from solve import solve

DATA_DIR = ASSIGNMENT_DIR / "data" / "Realistic"


class TestRealistic(unittest.TestCase):

    def _test_realistic(self, num: int):
        with open(DATA_DIR / "Exercises" / f"exercise{num}.json", "r") as exercise_file:
            exercise = json.load(exercise_file)

        actual = solve(exercise)

        with open(DATA_DIR / "Answers" / f"answer{num}.json", "r") as answer_file:
            expected = json.load(answer_file)

        self.assertEqual(expected, actual)

    def test_realistic00(self):
        self._test_realistic(0)

    def test_realistic01(self):
        self._test_realistic(1)

    def test_realistic02(self):
        self._test_realistic(2)

    def test_realistic03(self):
        self._test_realistic(3)

    def test_realistic04(self):
        self._test_realistic(4)

    def test_realistic05(self):
        self._test_realistic(5)

    def test_realistic06(self):
        self._test_realistic(6)

    def test_realistic07(self):
        self._test_realistic(7)

    def test_realistic08(self):
        self._test_realistic(8)

    def test_realistic09(self):
        self._test_realistic(9)

    def test_realistic10(self):
        self._test_realistic(10)

    def test_realistic11(self):
        self._test_realistic(11)

    def test_realistic12(self):
        self._test_realistic(12)

    def test_realistic13(self):
        self._test_realistic(13)


if __name__ == "__main__":
    unittest.main()