import sys

N = int(input())
max = -1
nums = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > max:
        max = num
    nums[num] += 1
for i in range(1, max + 1):
    for j in range(nums[i]):
        print(i)
