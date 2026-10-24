import unittest
from app import add
class Addition(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
