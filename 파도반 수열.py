# https://www.acmicpc.net/problem/9461
memo = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
memo += [0 for _ in range(90)]

def dp(n):
    if n > 10:
        if memo[n] == 0:
            memo[n] = dp(n - 1) + dp(n - 5)
    return memo[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp(N))