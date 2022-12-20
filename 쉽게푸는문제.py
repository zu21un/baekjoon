import sys
input = sys.stdin.readline

A, B = map(int, input().split())

result = 0
nums = [0]

num = 1
while len(nums) <= B:
  for i in range(num):
    nums.append(num)
  num += 1
  
print(sum(nums[A:B+1]))