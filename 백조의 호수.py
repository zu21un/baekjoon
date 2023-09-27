import sys

sys.setrecursionlimit = 1000000
input = sys.stdin.readline

R, C = map(int, input().split())
lake = []
swans = []
for i in range(R):
    line = list(input().strip())
    for j in range(C):
        if line[j] == "L":
            swans.append([i, j])
            line[j] = "."
    lake.append(line)

day = 0


def melt():
    global lake
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(R):
        for y in range(C):
            if lake[x][y] == ".":
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                if lake[nx][ny] == ".":
                    lake[x][y] = "O"
                    break
    for x in range(R):
        for y in range(C):
            if lake[x][y] == "O":
                lake[x][y] = "."


def dfs(x, y, x2, y2, is_visited):
    global lake
    if x == x2 and y == y2:
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if is_visited[nx][ny]:
            continue
        if lake[nx][ny] == "X":
            continue
        is_visited[nx][ny] = True
        dfs(nx, ny, x2, y2, is_visited)


def check():
    global swans
    x1, y1 = swans[0]
    x2, y2 = swans[1]
    is_visited = [[False for _ in range(C)] for _ in range(R)]
    is_visited[x1][y1] = True
    dfs(x1, y1, x2, y2, is_visited)

    return is_visited[x2][y2]


while not check():
    melt()
    day += 1

print(day)
