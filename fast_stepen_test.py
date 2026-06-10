import unittest

MOD = 10**9 + 7


def fast_power(a, n):
    if n == 0:
        return 1

    half = fast_power(a, n // 2)

    if n % 2 == 0:
        return (half * half) % MOD
    else:
        return (half * half * a) % MOD


class TestFastPower(unittest.TestCase):
    def test_example(self):
        self.assertEqual(fast_power(2, 10), 1024)

    def test_zero_power(self):
        self.assertEqual(fast_power(5, 0), 1)

    def test_big_power(self):
        self.assertEqual(fast_power(2, 100), pow(2, 100, MOD))


if __name__ == "__main__":
    unittest.main()