import unittest

from app import add


class Addition(unittest.TestCase):
    def test_positive_operands(self) -> None:
        self.assertEqual(add(3, 5), 8)

    def test_negative_operands(self) -> None:
        self.assertEqual(add(-3, -5), -8)

    def test_mixed_sign_operands(self) -> None:
        for a, b, expected in [(7, -3, 4), (-7, 3, -4), (-3, 7, 4), (3, -7, -4), (5, -5, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

    def test_zero_operands(self) -> None:
        for a, b, expected in [(0, 0, 0), (0, 6, 6), (6, 0, 6), (0, -6, -6), (-6, 0, -6)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)


if __name__ == "__main__":
    unittest.main()
