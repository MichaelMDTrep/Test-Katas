import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        out = add(x, y)
        assert out == 6
        self.fail("Test")

    def test_multiply(self):
        self.fail("TODO: Write multiply unit test")

    def test_power(self):
        self.fail("TODO: Write power unit test")

    def test_factorial(self):
        self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
