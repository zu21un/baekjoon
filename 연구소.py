import sys
import copy
input = sys.stdin.readline
from collections import deque

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())

board = []
virus = []
result = 0

for row in range(N):
  line = list(map(int, input().split()))
  for col in range(M):
    if line[col] == 2:
      virus.append((row, col))
    
  board.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(new_board, queue):
  while queue:
    row, col = queue.popleft()
    for i in range(4):
      x = row + dx[i]
      y = col + dy[i]
      if 0 <= x < N and 0 <= y < M and new_board[x][y] == 0:
        new_board[x][y] = 2
        queue.append((x,y))
      
  safe_zone = 0
  for row in range(N):
    safe_zone += new_board[row].count(0)
    
  return safe_zone

def make_wall(cnt):
  global result, board
  if cnt == 3:
    new_board = copy.deepcopy(board)
    result = max(bfs(new_board, deque(virus[:])), result)
    return
  else:
    for row in range(N):
      for col in range(M): 
        if board[row][col] == 0:
          board[row][col] = 1
          make_wall(cnt + 1)
          board[row][col] = 0

make_wall(0)
print(result)
