import sys
from collections import deque

input = sys.stdin.readline

N, M, H = map(int, input().split())

ladders = [[False for _ in range(N)] for _ in range(H + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    ladders[a][b] = True

origin_ladders = [line[:] for line in ladders]


def check():
    for i in range(1, N + 1):
        c = i
        r = 1
        while r <= H:
            if c - 1 >= 0 and ladders[r][c - 1] == True:
                c -= 1
            elif c < N and ladders[r][c] == True:
                c += 1
            r += 1
        if c != i:
            return False

    return True


def can_add(r, c):
    if ladders[r][c] == True:
        return False
    if c - 1 >= 0 and ladders[r][c - 1] == True:
        return False
    if c + 1 < N and ladders[r][c + 1] == True:
        return False
    return True


def add_ladders(lines):
    for line in lines:
        r, c = line
        ladders[r][c] = True


def reset():
    for i in range(H + 1):
        for j in range(N):
            ladders[i][j] = origin_ladders[i][j]


def find_next(line):
    r, c = line
    for i in range(1, H + 1):
        for j in range(N):
            if i * N + j <= r * N + c:
                continue
            if can_add(i, j):
                return [i, j]
    return False


if check():
    print(0)

else:

