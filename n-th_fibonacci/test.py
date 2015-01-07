import unittest

from solution import nth_fib

class test(unittest.TestCase):

    def test_nth_fib(self):
        self.assertEqual(nth_fib(1), 0)
        self.assertEqual(nth_fib(2), 1)
        self.assertEqual(nth_fib(3), 1)
        self.assertEqual(nth_fib(4), 2)
        self.assertEqual(nth_fib(5), 3)
        self.assertEqual(nth_fib(6), 5)
        self.assertEqual(nth_fib(7), 8)
        self.assertEqual(nth_fib(8), 13)
        self.assertEqual(nth_fib(9), 21)
        self.assertEqual(nth_fib(10), 34)
        self.assertEqual(nth_fib(11), 55)
        self.assertEqual(nth_fib(12), 89)
        self.assertEqual(nth_fib(13), 144)
        self.assertEqual(nth_fib(14), 233)
        self.assertEqual(nth_fib(15), 377)
        self.assertEqual(nth_fib(16), 610)
        self.assertEqual(nth_fib(17), 987)
        self.assertEqual(nth_fib(18), 1597)
        self.assertEqual(nth_fib(19), 2584)
        self.assertEqual(nth_fib(20), 4181)
        self.assertEqual(nth_fib(21), 6765)
        self.assertEqual(nth_fib(22), 10946)
        self.assertEqual(nth_fib(23), 17711)
        self.assertEqual(nth_fib(24), 28657)
        self.assertEqual(nth_fib(25), 46368)


if __name__ == '__main__':
    unittest.main()