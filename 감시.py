import sys
from collections import defaultdict

input = sys.stdin.readline

# 위 / 오른쪽 / 아래 / 왼쪽
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

dir_dict = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

cctv_dir = defaultdict(list)
cctv_dir[1].append([UP])
cctv_dir[1].append([RIGHT])
cctv_dir[1].append([DOWN])
cctv_dir[1].append([LEFT])

cctv_dir[2].append([UP, DOWN])
cctv_dir[2].append([LEFT, RIGHT])

cctv_dir[3].append([UP, RIGHT])
cctv_dir[3].append([RIGHT, DOWN])
cctv_dir[3].append([DOWN, LEFT])
cctv_dir[3].append([LEFT, UP])

cctv_dir[4].append([UP, RIGHT, DOWN])
cctv_dir[4].append([RIGHT, DOWN, LEFT])
cctv_dir[4].append([DOWN, LEFT, UP])
cctv_dir[4].append([LEFT, UP, RIGHT])

cctv_dir[5].append([UP, RIGHT, DOWN, LEFT])

N, M = map(int, input().split())

office = []
for _ in range(N):
    office.append(list(map(int, input().split())))

cctvs = []
for i, line in enumerate(office):
    for j, v in enumerate(line):
        if v != 0 and v != 6:
            cctvs.append([i, j])


def copy(office):
    return [line[:] for line in office]


def compute(office):
    cnt = 0
    for line in office:
        for v in line:
            if v == 0:
                cnt += 1
    return cnt


def fill(office, dx, dy, r, c):
    nx, ny = r + dx, c + dy
    while 0 <= nx < N and 0 <= ny < M:
        if office[nx][ny] == 6:
            break
        elif office[nx][ny] == 0:
            office[nx][ny] = -1
        nx += dx
        ny += dy


answer = float("inf")
stack = []
stack.append((cctvs[:], copy(office)))

while stack:
    cctvs, office = stack.pop()
    if len(cctvs) == 0:
        answer = min(answer, compute(office))
        continue

    r, c = cctvs.pop()
    cctv_num = office[r][c]

    for dirs in cctv_dir[cctv_num]:
        new_office = copy(office)
        for dir in dirs:
            dx, dy = dir_dict[dir]
            fill(new_office, dx, dy, r, c)
        stack.append((cctvs[:], new_office))

print(answer)
