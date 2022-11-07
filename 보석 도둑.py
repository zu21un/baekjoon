import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
for _ in range(N):
  M, V = map(int, input().split())
  weight, price = M, V
  heapq.heappush(jewels,(-price, weight, price))

bags = []
for _ in range(K):
  weight = int(input())
  bags.append(weight)
  
bags.sort()

result = 0
tmp = []
for bag in bags:
  while jewels:
    jewel = heapq.heappop(jewels)
    weight, price = jewel[1], jewel[2]
    if weight <= bag:
      result += price
      break
    else:
      tmp.append([weight, price])
  for weight, price in tmp:
    heapq.heappush(jewels,(-price, weight, price))
  tmp = []

print(result)

