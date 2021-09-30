# https://www.acmicpc.net/problem/2470

import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
left, right = 0, N - 1
result = float('inf')
answer = (float('inf'), float('inf'))
while left < right:
    sum = nums[left] + nums[right]
    if abs(sum) < abs(result):
        result = sum
        answer = (nums[left], nums[right])
        if sum == 0: break
    if nums[left] >= 0:
        right -= 1
    elif nums[right] <= 0:
        left += 1
    else:
        if sum < 0:
            left += 1
        else:
            right -= 1
print(answer[0], answer[1])

