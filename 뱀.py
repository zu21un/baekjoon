import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

SNAKE = 100
APPLE = 200
# 0: 오른쪽  1: 아래  2: 왼쪽  3: 위
dir_dict = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
# 처음에 오른쪽 방향
dir = 0
time = 0
hx = hy = 1
board[1][1] = SNAKE
is_finish = False

snake = deque()
snake.append([hx, hy])


def move():
    global time, hx, hy, dir
    time += 1
    dx, dy = dir_dict[dir]
    nx, ny = hx + dx, hy + dy
    if nx < 1 or nx > N or ny < 1 or ny > N or board[nx][ny] == SNAKE:
        return False

    hx, hy = nx, ny

    if board[hx][hy] == 0:
        tx, ty = snake.popleft()
        board[tx][ty] = 0
    board[hx][hy] = SNAKE
    snake.append([hx, hy])

    return True


K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = APPLE

L = int(input())
cmds = []
for _ in range(L):
    cmds.append(list(input().rstrip().split()))

for cmd in cmds:
    X, C = cmd
    X = int(X)
    while time < X:
        is_finish = True if not move() else False
        if is_finish:
            break
    if is_finish:
        break
    if C == "D":
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4

while not is_finish:
    is_finish = True if not move() else False

print(time)
