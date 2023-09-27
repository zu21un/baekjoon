from itertools import combinations

N, M = map(int, input().split())

city = []

houses = []
chickens = []

for i in range(N):
    line = list(map(int, input().split()))
    for j, v in enumerate(line):
        if v == 1:
            houses.append([i, j])
        elif v == 2:
            chickens.append([i, j])
    city.append(line)

dists = []
for house in houses:
    hx, hy = house
    dist = []
    for i, chicken in enumerate(chickens):
        cx, cy = chicken
        d = abs(hx - cx) + abs(hy - cy)
        dist.append((d, i))
    dist = sorted(dist)
    dists.append(dist)

# 남겨질 치킨 집 개수 고르기
min_dist = float("inf")
for i in range(1, M + 1):
    combs = combinations(range(len(chickens)), i)
    for comb in combs:
        ans = 0
        for dist in dists:
            for d, n in dist:
                if n in comb:
                    ans += d
                    break
        min_dist = min(min_dist, ans)

print(min_dist)
