import sys
import heapq

input = sys.stdin.readline

N = int(input())


heap = []  
for _ in range(N):
  d, w = map(int, input().split())
  day, score = d, w
  heapq.heappush(heap, (-day, score))

max_day = -heap[0][0]
current_day = max_day
able = []
result = 0

while current_day > 0:
  while heap and -heap[0][0] >= current_day:
    (day, score) = heapq.heappop(heap)
    day = -day
    heapq.heappush(able, (-score, day))
  
  if able:
    (score, day) = heapq.heappop(able)
    score = -score
    result += score
    
    for (score, day) in able:
      score = -score
      heapq.heappush(heap, (-day, score))
    able = []
    
  current_day -= 1

print(result)

