# 큰물고기 x
# 같은 물고기: 지나가기만
# 작은 물고기: 지나가기 + 먹기

from collections import deque

N = int(input())

area = []
for _ in range(N):
    area.append(list(map(int, input().split())))

shark_x = shark_y = None
eat_cnt = 0
size = 2
time = 0

for r in range(N):
    for c in range(N):
        if area[r][c] == 9:
            shark_x, shark_y = r, c
            area[r][c] = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def find_fish():
    # 현 위치 + 이동한 횟수
    global shark_x, shark_y, size, time, eat_cnt
    is_visited = [[False for _ in range(N)] for _ in range(N)]
    stack1 = []
    stack2 = []
    can_eat = []
    stack2.append((shark_x, shark_y, 0))
    is_visited[shark_x][shark_y] = True
    while stack2:
        stack1 = stack2
        stack2 = []
        while stack1:
            x, y, d = stack1.pop()

            if 1 <= area[x][y] < size:
                can_eat.append((x, y, d))
                continue

            # 다음 갈 곳 찾기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if area[nx][ny] > size or is_visited[nx][ny]:
                    continue
                stack2.append((nx, ny, d + 1))
                is_visited[nx][ny] = True

        if can_eat:
            can_eat = sorted(can_eat)
            x, y, d = can_eat[0]
            shark_x, shark_y = x, y
            area[x][y] = 0
            eat_cnt += 1
            if eat_cnt == size:
                size += 1
                eat_cnt = 0
            time += d
            return True

    return False


while find_fish():
    continue

print(time)
