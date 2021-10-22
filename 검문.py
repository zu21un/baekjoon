from itertools import combinations

N = int(input())
nums = []
difs = []
for _ in range(N):
    nums.append(int(input()))
for a, b in combinations(nums, 2):
    difs.append(abs(a - b))
difs = list(set(difs))
difs.sort()
result = []
for i in range(2, difs[0] + 1):
    for dif in difs:
        if dif % i != 0:
            break
    else:
        result.append(i)
print(' '.join(map(str, result)))