import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEquals(Calculator.add(5, 3), 8)

    def test_sub(self):
        self.assertEquals(Calculator.sub(5, 3), 2)


if __name__ == "__main__":
    unittest.main()