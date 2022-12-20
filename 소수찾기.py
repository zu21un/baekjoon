import sys
import math
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

def get_prime_list(max_num):
  primes = [True] * (max_num + 1)
  primes[0] = primes[1] = False
  
  num = int(math.sqrt(max_num))
  
  for i in range(2, num + 1):
    if primes[i] == True:
      for j in range(i + i, max_num + 1, i):
        primes[j] = False
  
  return primes

prime_nums = get_prime_list(max(nums))
result = 0

for num in nums:
  if prime_nums[num] == True:
    result += 1

print(result)