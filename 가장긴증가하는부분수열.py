import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = []

for i1, v1 in enumerate(seq):
    dp.append(1)
    for i2, v2 in enumerate(seq[:i1]):
        if v2 < v1:
            dp[i1] = max(dp[i1], dp[i2] + 1)
            
print(max(dp))