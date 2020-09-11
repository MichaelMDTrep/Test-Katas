import unittest
import katas
import random
import math


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertTrue(katas.add)
        for _ in range(0, 10):
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            self.assertAlmostEqual(katas.add(x, y), x + y)

    def test_multiply(self):
        self.assertTrue(katas.multiply)
        self.assertTrue(katas.multiply(-2, 3) == -6)
        self.assertTrue(katas.multiply(2, -3) == -6)
        self.assertTrue(katas.multiply(-2, -3) == 6)
        self.assertTrue(katas.multiply(2, 3) == 6)
        for _ in range(10):
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            self.assertAlmostEqual(katas.multiply(x, y), x * y)

    def test_power(self):
        self.assertTrue(katas.power)
        self.assertTrue(katas.power(3, 4) == 3 ** 4)
        self.assertTrue(katas.power(62, 0) == 1)
        self.assertTrue(katas.power(-2, 3) == -2 ** 3)
        for _ in range(10):
            x = random.randint(-10, 10)
            y = random.randint(0, 10)
            self.assertTrue(katas.power(x, y) == x ** y)

    def test_factorial(self):

        self.assertTrue(katas.factorial)
        self.assertTrue(katas.factorial(4) == math.factorial(4))
        for x in range(10):
            self.assertTrue(katas.factorial(x) == math.factorial(x))

    def test_fibonacci(self):

        self.assertTrue(katas.fibonacci)
        fibs = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
        for n in range(11):
            self.assertTrue(katas.fibonacci(n) == fibs[n])


if __name__ == '__main__':
    unittest.main()
