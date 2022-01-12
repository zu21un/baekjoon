import sys
input = sys.stdin.readline

N = int(input())

dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

rest_dist = sum(dist)

result = 0

min_cost = cost[0]
min_idx = 0
for i in range(1, len(dist)):
    if cost[i] <= min_cost:
        sum(dist[min_idx:i])