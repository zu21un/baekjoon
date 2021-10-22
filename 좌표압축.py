import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
sorted_nums = sorted(list(set(nums)))
dict = {}
for i, v in enumerate(sorted_nums):
    dict[v] = i
for i in range(len(nums)):
    nums[i] = dict[nums[i]]
print(' '.join(map(str,nums)))
    
