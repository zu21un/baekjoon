import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

def fibo(num):
  if num >= 2 and dp[num] == 0:
    dp[num] = fibo(num - 1) + fibo(num - 2)
  return dp[num]
  
print(fibo(n))