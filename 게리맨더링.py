import sys
from collections import defaultdict

input = sys.stdin.readline

def dfs(graph, root, visit_count):
  visited = []
  stack = [root]

  count = 0
  while stack and count < visit_count:
    n = stack.pop()
    if n not in visited:
      visited.append(n)
      stack += set(graph[n]) - set(visited)
      count += 1
  return visited

N = int(input())
populations = list(map(int, input().split()))

whole_people_count = sum(populations)

area_graph = defaultdict(list)
for i in range(1, N+1):
  adjacents = list(map(int, input().split()))
  area_graph[i] = adjacents[1:]

print(dfs(area_graph, 1, 1))
print(dfs(area_graph, 1, 2))
print(dfs(area_graph, 1, 3))
print(dfs(area_graph, 1, 4))
print(dfs(area_graph, 1, 5))
print(dfs(area_graph, 1, 6))

      
  