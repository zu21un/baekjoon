import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
K = int(input())

graph = {i: {} for i in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, input().split())
    if v not in graph[u]:
        graph[u][v] = w
    else:
        if graph[u][v] > w:
            graph[u][v] = w

def dijkstra(graph, start):
    dists = {node: float('inf') for node in graph}
    dists[start] = 0
    queue = []
    heapq.heappush(queue, [dists[start], start])
    
    while queue:
        current_dist, current_dest = heapq.heappop(queue)
        
        if dists[current_dest] < current_dist:
            continue
        
        for new_dest, new_dist in graph[current_dest].items():
            dist = current_dist + new_dist
            if dist < dists[new_dest]:
                dists[new_dest] = dist
                heapq.heappush(queue, [dist, new_dest])
    
    return dists

result = dijkstra(graph, K)

for i in range(1, len(result)+1):
    if result[i] == float('inf'):
        print('INF')
    else:
        print(result[i])

    