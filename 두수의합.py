# https://www.acmicpc.net/problem/3273

n = int(input())

nums = list(map(int, input().split()))
nums.sort()
target = int(input())
left, right = 0, n - 1
result = 0

while left < right:
    sum = nums[left] + nums[right]
    if sum == target:
        result += 1
        left += 1
        right -= 1
    elif sum < target:
        left += 1
    else:
        right -= 1
print(result)