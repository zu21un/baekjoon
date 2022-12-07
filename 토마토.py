import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())

storage = []

date = 0
not_riped = 0
riped = deque([])

for i in range(N):
  tomatos = list(map(int, input().split()))
  for j in range(M):
    if tomatos[j] == 1:
      riped.append((i, j))
    elif tomatos[j] == 0:
      not_riped += 1
  storage.append(tomatos)

while not_riped:
  date += 1
  new_riped = deque([])
  
  while riped:
    row, col = riped.popleft()
    
    if row - 1 >= 0 and storage[row-1][col] == 0:
      storage[row-1][col] = 1
      not_riped -= 1
      new_riped.append((row - 1, col))
    if col - 1 >= 0 and storage[row][col-1] == 0:
      storage[row][col-1] = 1
      not_riped -= 1
      new_riped.append((row, col - 1))
    if row + 1 < N and storage[row+1][col] == 0:
      storage[row+1][col] = 1
      not_riped -= 1
      new_riped.append((row + 1, col))
    if col + 1 < M and storage[row][col+1] == 0:
      storage[row][col+1] = 1
      not_riped -= 1
      new_riped.append((row, col + 1))

  if len(new_riped) == 0:
    break
  
  riped = new_riped
  

if not_riped == 0:
  print(date)
else:
  print(-1)
