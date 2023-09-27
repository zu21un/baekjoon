# 100 * 100
# 100초 까지

from collections import defaultdict
from collections import Counter

A = [[0 for _ in range(101)] for _ in range(101)]


r, c, k = map(int, input().split())
for i in range(1, 4):
    line = list(map(int, input().split()))
    for j, v in enumerate(line):
        A[i][j + 1] = v

time = 0
max_R = 3
max_C = 3


def row():
    global max_C
    max_c = max_C
    for r in range(1, max_R + 1):
        d = defaultdict(int)
        for c in range(1, max_C + 1):
            v = A[r][c]
            d[v] += 1
            A[r][c] = 0
        result = compute(d)
        i = 0
        while i < len(result) and i < 100:
            A[r][i + 1] = result[i]
            i += 1
        max_c = max(max_c, len(result))
    max_C = max(max_C, max_c)


def column():
    global max_R

    max_r = max_R
    for c in range(1, max_C + 1):
        d = defaultdict(int)
        for r in range(1, max_R + 1):
            v = A[r][c]
            d[v] += 1
            A[r][c] = 0
        result = compute(d)
        i = 0
        while i < len(result) and i < 100:
            A[i + 1][c] = result[i]
            i += 1
        max_r = max(max_r, len(result))
    max_R = max(max_R, max_r)


def compute(d):
    arr = []
    for a, b in d.items():
        arr.append((a, b))
    arr = sorted(arr, key=lambda x: (x[1], x[0]))
    result = []
    for v in arr:
        a, b = v
        if a == 0:
            continue
        result.append(a)
        result.append(b)

    return result


while time <= 100:
    if r <= max_R and c <= max_C and A[r][c] == k:
        print(time)
        break
    if max_R >= max_C:
        row()
    else:
        column()
    time += 1

else:
    print(-1)
