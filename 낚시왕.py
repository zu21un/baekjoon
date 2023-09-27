import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[None for _ in range(C + 1)] for _ in range(R + 1)]

dir_dict = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, 1],
    4: [0, -1],
}

# s = 속력, d = 방향, z = 크기
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c] = (s, d, z)

cnt = 0


def catch(c):
    size = 0
    r = 0
    while r < R:
        r += 1
        if board[r][c] == None:
            continue

        s, d, z = board[r][c]
        size += z
        board[r][c] = None
        break

    return size


def turn(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    elif d == 4:
        return 3


def move():
    global board
    moved_sharks = []

    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if board[r][c] == None:
                continue
            s, d, z = board[r][c]
            x, y = r, c

            dx, dy = dir_dict[d]
            dist = s % abs(dx * 2 * (R - 1) + dy * 2 * (C - 1))

            while dist > 0:
                nx, ny = x + dx * dist, y + dy * dist
                if 1 <= nx <= R and 1 <= ny <= C:
                    x, y = nx, ny
                    break
                if dx != 0:
                    nx = max(0, dx) * (R - 1) + 1
                    ny = y
                if dy != 0:
                    nx = x
                    ny = max(0, dy) * (C - 1) + 1
                dist -= max(x, nx) - min(x, nx) + max(y, ny) - min(y, ny)
                d = turn(d)
                dx, dy = dir_dict[d]
                x, y = nx, ny

            moved_sharks.append((x, y, s, d, z))
            board[r][c] = None
    for shark in moved_sharks:
        r, c, s, d, z = shark
        if board[r][c] == None or board[r][c][2] < z:
            board[r][c] = (s, d, z)


for c in range(1, C + 1):
    cnt += catch(c)
    move()

print(cnt)
