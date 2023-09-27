import sys

input = sys.stdin.readline

dir_dict = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1]}

sharks = {}
shark_dir = {}
# M: 상어 마리 수
# k: 냄새 유지
N, M, k = map(int, input().split())
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]

# board: 3차원 배열
# smell: 3차원 배열

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] > 0:
            shark = line[j]
            sharks[shark] = [i, j]

dirs = [0] + list(map(int, input().split()))

for n in range(1, M + 1):
    d = {}
    for i in range(1, 5):
        d[i] = list(map(int, input().split()))
    shark_dir[n] = d

time = 0

for i, v in sharks.items():
    r, c = v
    smell[r][c][0], smell[r][c][1] = i, k

while time <= 1000:
    if len(list(sharks.keys())) == 1:
        break
    time += 1

    board = [[[] for _ in range(N)] for _ in range(N)]
    for shark, v in sharks.items():
        x, y = v
        d = dirs[shark]
        dir_order = shark_dir[shark][d]
        # 냄새가 없는 지 확인
        for nd in dir_order:
            dx, dy = dir_dict[nd]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if smell[nx][ny][0] != 0:
                continue
            board[nx][ny].append(shark)
            dirs[shark] = nd
            break
        else:
            # 자신의 냄새가 있는 곳으로 이동
            for nd in dir_order:
                dx, dy = dir_dict[nd]
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if smell[nx][ny][0] != shark:
                    continue
                board[nx][ny].append(shark)
                dirs[shark] = nd
                break

    sharks = {}
    for i in range(N):
        for j in range(N):
            board[i][j] = sorted(board[i][j])[:1]
            if len(board[i][j]) == 0:
                continue
            shark = board[i][j][0]
            sharks[shark] = [i, j]

    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0
    for i, v in sharks.items():
        r, c = v
        smell[r][c][0], smell[r][c][1] = i, k

print(time) if time <= 1000 else print(-1)
