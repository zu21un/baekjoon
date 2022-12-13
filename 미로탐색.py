import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
  line = list(map(int, input().strip()))
  board.append(line)

print(board)

def bfs(row, col):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  queue = deque()
  queue.append((row, col))
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M:
        if board[nx][ny] == 1:
          board[nx][ny] = board[x][y] + 1
          queue.append((nx, ny))
  
  return board[N-1][M-1]

print(board)

print(bfs(0,0))