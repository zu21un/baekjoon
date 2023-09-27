# 같은 칸에 여러 개의 나무 가능

# r, c 1부터 시작

import heapq
from collections import deque

N, M, K = map(int, input().split())

land = [[deque() for _ in range(N + 1)] for _ in range(N + 1)]

A = [[0 for _ in range(N + 1)]]

for _ in range(N):
    line = list(map(int, input().split()))
    line = [0] + line
    A.append(line)

food = [[5 for _ in range(N + 1)] for _ in range(N + 1)]
dead = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    x, y, age = map(int, input().split())
    l = land[x][y]
    l.append(age)

for line in land:
    line = sorted(line)


# 봄:
# 자신의 나이만큼 양분
# 나이 + 1
# 어린 나무 부터 양분 먹음
# 못먹으면 바로 죽음
def spring():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            trees = land[r][c]
            for i in range(len(trees)):
                if trees[i] <= food[r][c]:
                    food[r][c] -= trees[i]
                    trees[i] += 1
                else:
                    for _ in range(i, len(trees)):
                        dead[r][c].append(trees.pop())
                    break


# 여름:
# 봄에 죽은 나무가 양분
# 나이를 2로 나눈 값
# 소수점 버림
def summer():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            d = dead[r][c]
            for age in d:
                food[r][c] += age // 2
            dead[r][c] = []


# 가을:
# 번식
# 나이가 5의 배수
# 인접한 8개 칸에 나이가 1인 나무 생김
def autumn():
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            trees = land[r][c]
            for age in trees:
                if age % 5 == 0:
                    for d in dirs:
                        dr, dc = d
                        nr, nc = r + dr, c + dc
                        if nr < 1 or nr > N or nc < 1 or nc > N:
                            continue
                        land[nr][nc].appendleft(1)


# 겨울:
# 양분 추가
# 입력으로 주어짐
def winter():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            food[r][c] += A[r][c]


def check():
    cnt = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            cnt += len(land[r][c])

    return cnt


for _ in range(K):
    spring()
    summer()
    autumn()
    winter()

cnt = check()

print(cnt)
