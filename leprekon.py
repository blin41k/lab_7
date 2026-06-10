n, m = map(int, input().split())
weights = list(map(int, input().split()))

dp = [False] * (m + 1)
dp[0] = True

for weight in weights:
    for current in range(m, weight - 1, -1):
        if dp[current - weight]:
            dp[current] = True

for answer in range(m, -1, -1):
    if dp[answer]:
        print(answer)
        break