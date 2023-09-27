import sys

input = sys.stdin.readline
from itertools import combinations

# 0: 빈 칸, 1: 벽, 2: 바이러스

EMPTY = 0
WALL = 1
VIRUS = 2
VIRUS_ACTIVE = 3

EMPTY_COUNT_DEFAULT = 0
WALL_COUNT_DEFAULT = 0
VIRUS_COUNT_DEFAULT = 0

EMPTY_COUNT = 0
WALL_COUNT = 0
VIRUS_COUNT = 0


N, M = map(int, input().split())

lab = []
viruses = []
viruses_active = []

for _ in range(N):
    lab.append(list(map(int, input().split())))

for r in range(N):
    for c in range(N):
        if lab[r][c] == VIRUS:
            viruses.append((r, c))
            VIRUS_COUNT_DEFAULT += 1
        elif lab[r][c] == WALL:
            WALL_COUNT_DEFAULT += 1
        elif lab[r][c] == EMPTY:
            EMPTY_COUNT_DEFAULT += 1

combs = combinations(range(len(viruses)), M)


def spread():
    global VIRUS_COUNT, WALL_COUNT, EMPTY_COUNT, viruses_active

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    add_viruses = []

    for virus in viruses_active:
        x, y = virus
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if lab[nx][ny] == WALL or lab[nx][ny] == VIRUS_ACTIVE:
                continue
            if lab[nx][ny] == EMPTY:
                VIRUS_COUNT += 1
                EMPTY_COUNT -= 1
            lab[nx][ny] = VIRUS_ACTIVE
            add_viruses.append((nx, ny))
    viruses_active = add_viruses
    return True if len(add_viruses) > 0 else False


def check():
    if EMPTY_COUNT != 0:
        return False

    return True


def set_default():
    global VIRUS_COUNT, EMPTY_COUNT, WALL_COUNT, viruses_active
    for r in range(N):
        for c in range(N):
            if lab[r][c] == WALL:
                continue
            lab[r][c] = EMPTY
    for virus in viruses:
        r, c = virus
        lab[r][c] = VIRUS

    VIRUS_COUNT = VIRUS_COUNT_DEFAULT
    EMPTY_COUNT = EMPTY_COUNT_DEFAULT
    WALL_COUNT = WALL_COUNT_DEFAULT
    viruses_active = []


min_time = float("inf")

for comb in combs:
    # 초기화 및 활성 바이러스 세팅
    time = 0
    set_default()
    for idx in comb:
        virus = viruses[idx]
        r, c = virus
        lab[r][c] = VIRUS_ACTIVE
        viruses_active.append(virus)

    while not check() and spread():
        time += 1
        if time >= min_time:
            break
    if check():
        min_time = min(min_time, time)

if min_time < float("inf"):
    print(min_time)
else:
    print(-1)
