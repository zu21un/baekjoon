import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
rx = ry = bx = by = 0

for i in range(N):
    line = list(input().rstrip())
    for j, v in enumerate(line):
        if v == "R":
            rx = i
            ry = j
        elif v == "B":
            bx = i
            by = j
    board.append(line)


queue = deque([])
queue.append([rx, ry, bx, by, 0])

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

visited[rx][ry][bx][by] = True

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def move(x, y, dx, dy):
    count = 0
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    while queue:
        rx, ry, bx, by, count = queue.popleft()

        if count + 1 > 10:
            break
        for i in range(4):
            nrx, nry, rcount = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcount = move(bx, by, dx[i], dy[i])

            if board[nbx][nby] == "O":
                continue

            if board[nrx][nry] == "O":
                print(count + 1)
                return

            if nrx == nbx and nry == nby:
                if rcount < bcount:
                    nbx -= dx[i]
                    nby -= dy[i]
                else:
                    nrx -= dx[i]
                    nry -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append([nrx, nry, nbx, nby, count + 1])
    print(-1)


bfs()
