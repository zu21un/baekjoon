import sys
from collections import defaultdict, deque


input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)
dist = [-1 for _ in range(n + 1)]    
dist[1] = 0

def dfs(node, weight):
  for next_node, next_weight in graph[node]:
    if dist[next_node] == -1:
      dist[next_node] = weight + next_weight
      dfs(next_node, weight + next_weight)


for _ in range(n - 1):
  parent, child, weight = map(int, input().split())
  graph[parent].append((child, weight))
  graph[child].append((parent, weight))
  
dfs(1, 0)

start = dist.index(max(dist))

dist = [-1 for _ in range(n + 1)]    
dist[start] = 0
dfs(start, 0)

print(max(dist))