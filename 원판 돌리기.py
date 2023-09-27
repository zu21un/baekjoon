import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())

DEL = -100

plates = [[DEL for _ in range(M)]]


def check_adj(plates, i, j):
    num = plates[i][j]
    if num == DEL:
        return False
    if plates[i][(j - 1) % M] == num:
        return True
    if plates[i][(j + 1) % M] == num:
        return True
    if i > 1 and plates[i - 1][j] == num:
        return True
    if i < N and plates[i + 1][j] == num:
        return True
    return False


def remove_adj(plates, i, j):
    is_visited = [[False for _ in range(M)] for _ in range(N + 1)]
    stack = []
    stack.append((i, j))
    is_visited[i][j] = True
    num = plates[i][j]
    while stack:
        i, j = stack.pop()
        plates[i][j] = DEL

        if not is_visited[i][(j - 1) % M] and plates[i][(j - 1) % M] == num:
            stack.append((i, (j - 1) % M))
            is_visited[i][(j - 1) % M] = True
        if not is_visited[i][(j + 1) % M] and plates[i][(j + 1) % M] == num:
            stack.append((i, (j + 1) % M))
            is_visited[i][(j + 1) % M] = True
        if i > 1 and not is_visited[i - 1][j] and plates[i - 1][j] == num:
            stack.append((i - 1, j))
            is_visited[i - 1][j] = True
        if i < N and not is_visited[i + 1][j] and plates[i + 1][j] == num:
            stack.append((i + 1, j))
            is_visited[i + 1][j] = True


def set_plates(plates):
    sum = 0
    cnt = 0
    for i in range(1, N + 1):
        for j in range(M):
            num = plates[i][j]
            if num == DEL:
                continue
            sum += num
            cnt += 1
    if cnt <= 1:
        return

    mean = sum / cnt
    for i in range(1, N + 1):
        for j in range(M):
            num = plates[i][j]
            if num == DEL:
                continue
            if num > mean:
                plates[i][j] = num - 1
            elif num < mean:
                plates[i][j] = num + 1

    return


def get_plates_sum(plates):
    sum = 0
    for i in range(1, N + 1):
        for j in range(M):
            num = plates[i][j]
            if num == DEL:
                continue
            sum += num

    return sum


for _ in range(N):
    plate = deque(list(map(int, input().split())))
    plates.append(plate)

for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(x, N + 1, x):
        for j in range(k):
            if d == 0:
                plates[i].appendleft(plates[i].pop())
            else:
                plates[i].append(plates[i].popleft())

    is_deleted = False
    for i in range(1, N + 1):
        for j in range(M):
            if check_adj(plates, i, j) == True:
                is_deleted = True
                remove_adj(plates, i, j)
    if not is_deleted:
        set_plates(plates)

print(get_plates_sum(plates))
