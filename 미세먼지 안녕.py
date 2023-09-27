import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())

room = []

for _ in range(R):
    room.append(list(map(int, input().split())))

air_cleaner = []

for r in range(R):
    for c in range(C):
        if room[r][c] == -1:
            air_cleaner.append((r, c))


def diffusion():
    global room
    dust = [[0 for _ in range(C)] for _ in range(R)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for r in range(R):
        for c in range(C):
            if room[r][c] < 5:
                continue
            d = room[r][c] // 5
            for i in range(4):
                nx, ny = r + dx[i], c + dy[i]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                if room[nx][ny] == -1:
                    continue
                room[r][c] -= d
                dust[nx][ny] += d

    for r in range(R):
        for c in range(C):
            room[r][c] += dust[r][c]


def cycle():
    global air_cleaner
    a1, a2 = air_cleaner
    x1, x2 = a1[0], a2[0]

    r = x1 - 1
    while r > 0:
        room[r][0] = room[r - 1][0]
        r -= 1
    c = 0
    while c < C - 1:
        room[0][c] = room[0][c + 1]
        c += 1
    r = 0
    while r < x1:
        room[r][C - 1] = room[r + 1][C - 1]
        r += 1
    c = C - 1
    while c > 0:
        room[x1][c] = room[x1][c - 1]
        c -= 1
    room[x1][0], room[x1][1] = -1, 0

    r = x2 + 1
    while r < R - 1:
        room[r][0] = room[r + 1][0]
        r += 1

    c = 0
    while c < C - 1:
        room[R - 1][c] = room[R - 1][c + 1]
        c += 1

    r = R - 1
    while r > x2:
        room[r][C - 1] = room[r - 1][C - 1]
        r -= 1
    c = C - 1
    while c > 0:
        room[x2][c] = room[x2][c - 1]
        c -= 1
    room[x2][0], room[x2][1] = -1, 0


def check():
    global room
    cnt = 0
    for r in range(R):
        for c in range(C):
            cnt += room[r][c]
    return cnt + 2


for _ in range(T):
    diffusion()
    cycle()

print(check())
