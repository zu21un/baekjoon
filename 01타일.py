# https://www.acmicpc.net/problem/1904

N = int(input())
result = 0
memo = [1, 2]
if N == 1:
    result = 1
elif N == 2:
    result = 2
else:
    for i in range(3, N+1):
        result = (memo[0] + memo[1]) % 15746
        memo[0], memo[1] = memo[1], result
print(result)
    
