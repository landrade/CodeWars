import unittest

from solution import is_prime

class test(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(8), False)
        self.assertEqual(is_prime(9), False)
        self.assertEqual(is_prime(41), True)
        self.assertEqual(is_prime(45), False)
        self.assertEqual(is_prime(73), True)
        self.assertEqual(is_prime(75), False)
        self.assertEqual(is_prime(5099), True)
        self.assertEqual(is_prime(-1), False)


if __name__ == '__main__':
    unittest.main()