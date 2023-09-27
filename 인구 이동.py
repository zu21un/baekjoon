N, L, R = map(int, input().split())

A = []
is_visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    A.append(list(map(int, input().split())))


day = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def get_union(x, y):
    global is_visited
    if is_visited[x][y]:
        return False
    is_visited[x][y] = True
    u = [[x, y]]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if is_visited[nx][ny]:
            continue

        diff = abs(A[x][y] - A[nx][ny])
        if L <= diff <= R:
            nu = get_union(nx, ny)
            if nu:
                u += nu

    return u


def move(unions):
    for union in unions:
        p = 0
        for x, y in union:
            p += A[x][y]
        p = p // len(union)
        for x, y in union:
            A[x][y] = p


while day <= 2000:
    unions = []

    for r in range(N):
        for c in range(N):
            is_visited[r][c] = False

    for r in range(N):
        for c in range(N):
            if not is_visited[r][c]:
                union = get_union(r, c)
                if len(union) > 1:
                    unions.append(union)

    if len(unions) == 0:
        break

    move(unions)
    day += 1

print(day)
