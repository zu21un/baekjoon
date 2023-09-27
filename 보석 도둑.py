import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
for _ in range(N):
  M, V = map(int, input().split())
  weight, price = M, V
  heapq.heappush(jewels,(weight, price))

bags = []
for _ in range(K):
  weight = int(input())
  bags.append(weight)
  
bags.sort()

result = 0
tmp = []
for bag in bags:
  while jewels and bag >= jewels[0][0]:
    weight, price = heapq.heappop(jewels)
    heapq.heappush(tmp, (-price, weight))
  if tmp:
    price, weight = heapq.heappop(tmp)
    price = -price
    result += price
  elif not jewels:
    break
  
print(result)

