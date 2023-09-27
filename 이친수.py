N = int(input())

dp = [0 for _ in range(N + 1)]

dp[1] = 1


def get_pn(n):
    if n <= 1 or dp[n] > 0:
        return dp[n]

    dp[n] = 1 + get_pn(n - 2)
    return dp[n]


print(get_pn(N))
print(dp)
