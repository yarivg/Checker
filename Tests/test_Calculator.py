import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEquals(8, Calculator.add(self, 5, 3))

    def test_sub(self):
        self.assertEquals(2, Calculator.sub(self, 5, 3))

    def test_div(self):
        self.assertEquals(2, Calculator.div(self, 6, 3))
        self.assertRaises(ZeroDivisionError, lambda: Calculator.div(self, 5, 0))


if __name__ == "__main__":
    unittest.main()
