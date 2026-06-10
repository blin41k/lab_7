MOD = 10**9 + 7


def fast_power(a, n):
    if n == 0:
        return 1

    half = fast_power(a, n // 2)

    if n % 2 == 0:
        return (half * half) % MOD
    else:
        return (half * half * a) % MOD


a, n = map(int, input().split())
print(fast_power(a, n))