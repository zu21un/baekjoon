import sys
import collections
input = sys.stdin.readline

N = int(input())
T = int(input())
answer = 0
memo = [False for _ in range(T + 1)]
graph = collections.defaultdict(list)
for _ in range(T):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
while stack:
    virus = stack.pop()
    if memo[virus] == False:
        memo[virus] = True
        answer += 1
    for vertex in graph[virus]:
        if memo[vertex] == False:
            stack.append(vertex)
            
print(answer - 1)
    

