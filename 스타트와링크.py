import sys
from itertools import combinations, permutations

input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    l = list(map(int, input().split()))
    arr.append(l)

nums = [i for i in range(N)]
combi = list(combinations(nums, int(N/2)))

i, j = 0, len(combi) - 1
diff = float('inf')

while i < j:
    start = 0
    link = 0
    
    for a, b in permutations(combi[i], 2):
        start += arr[a][b]
    for a, b in permutations(combi[j], 2):
        link += arr[a][b]
        
    if abs(start - link) < diff:
        diff = abs(start - link)
    if diff == 0:
        break
    i += 1
    j -= 1

print(diff)