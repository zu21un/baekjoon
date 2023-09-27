N = int(input())

r = c = N // 2

board = []

out = 0

for _ in range(N):
    board.append(list(map(int, input().split())))


def move(sand, x, y):
    global board, out
    if x < 0 or x >= N or y < 0 or y >= N:
        out += sand
    else:
        board[x][y] += sand


def tornado(x1, y1, x2, y2):
    global board
    dx = x2 - x1
    dy = y2 - y1
    sand = board[x2][y2]
    if sand == 0:
        return
    # 1%
    sand_1 = sand // 100
    nx = x1 + dy
    ny = y1 + dx
    move(sand_1, nx, ny)
    nx = x1 - dy
    ny = y1 - dx
    move(sand_1, nx, ny)
    # 7%
    sand_7 = (sand * 7) // 100
    nx = x2 + dy
    ny = y2 + dx
    move(sand_7, nx, ny)
    nx = x2 - dy
    ny = y2 - dx
    move(sand_7, nx, ny)
    # 2%
    sand_2 = (sand * 2) // 100
    nx = x2 + (2 * dy)
    ny = y2 + (2 * dx)
    move(sand_2, nx, ny)
    nx = x2 - (2 * dy)
    ny = y2 - (2 * dx)
    move(sand_2, nx, ny)
    # 10%
    sand_10 = (sand * 10) // 100
    nx = x2 + dx + dy
    ny = y2 + dy + dx
    move(sand_10, nx, ny)
    nx = x2 + dx - dy
    ny = y2 + dy - dx
    move(sand_10, nx, ny)
    # 5%
    sand_5 = (sand * 5) // 100
    nx = x2 + (2 * dx)
    ny = y2 + (2 * dy)
    move(sand_5, nx, ny)
    # a%
    sand_a = sand - (2 * (sand_1 + sand_7 + sand_2 + sand_10) + sand_5)
    nx = x2 + dx
    ny = y2 + dy
    move(sand_a, nx, ny)

    board[x2][y2] = 0


tornado(r, c, r, c - 1)

c -= 1

cnt = 1

while 0 <= r < N and 0 <= c < N:
    for i in range(cnt):
        tornado(r, c, r + 1, c)
        r += 1
    for j in range(cnt + 1):
        tornado(r, c, r, c + 1)
        c += 1
    for k in range(cnt + 1):
        tornado(r, c, r - 1, c)
        r -= 1
    for l in range(cnt + 2):
        tornado(r, c, r, c - 1)
        c -= 1

    cnt += 2


print(out)
