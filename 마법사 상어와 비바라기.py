import sys

input = sys.stdin.readline


N, M = map(int, input().split())

board = []

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(N):
    board.append(list(map(int, input().split())))

clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for cloud in clouds:
    r, c = cloud


def copy_water(r, c, board):
    global N
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if board[nr][nc] > 0:
            board[r][c] += 1


for _ in range(M):
    cloud_board = [[False for _ in range(N)] for _ in range(N)]

    d, s = map(int, input().split())
    for i, cloud in enumerate(clouds):
        x, y = cloud
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        board[nx][ny] += 1
        cloud_board[nx][ny] = True
        clouds[i] = (nx, ny)
    for i, cloud in enumerate(clouds):
        x, y = cloud
        copy_water(x, y, board)

    clouds = []
    for i in range(N):
        for j in range(N):
            if board[i][j] < 2 or cloud_board[i][j] == True:
                continue

            board[i][j] -= 2
            clouds.append((i, j))
            cloud_board[i][j] = True

result = 0
for i in range(N):
    for j in range(N):
        result += board[i][j]

print(result)
