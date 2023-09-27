import sys

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
  board.append(map(int, input().split()))
  
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def move(board, dx, dy):
  x = y = 0
  if dx > 0:
    x = N - 1
  if dy > 0:
    y = N - 1

  while 0 <= x < N and 0 <= y < N:
    x -= dx
    y -= dy
    
    if board[x][y] == 0:
      continue
    
    nx = x
    ny = y
    while 0 <= nx + dx < N and 0 <= ny + dy < N and board[nx][ny] == 0:
      nx += dx
      ny += dy
    
    if 0 <= nx + dx < N and 0 <= ny + dy < N:
      if board[nx + dx][ny + dy] == board[nx][ny]:
        board[nx + dx][ny + dy] *= 2
        
      else:
      
    x -= dx
    y -= dy