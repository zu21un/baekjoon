import sys
input = sys.stdin.readline

N = int(input())

nums = sorted(list(map(int, input().split())))

print(min(nums), max(nums))