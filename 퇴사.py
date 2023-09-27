import sys

input = sys.stdin.readline


N = int(input())
reserves = []
for _ in range(N):
    reserves.append(list(map(int, input().split())))

dp = [-1 for _ in range(N)]


def get(day):
    if day >= N:
        return 0

    if dp[day] != -1:
        return dp[day]

    fee = 0
    T, P = reserves[day]
    next_day = day + T

    if next_day - 1 < N:
        fee = P + get(next_day)

    for d in range(day + 1, next_day):
        fee = max(fee, get(d))

    dp[day] = fee

    return fee


print(get(0))
