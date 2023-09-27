N, Q = map(int, input().split())

board = []
for _ in range(2**N):
    board.append(list(map(int, input().split())))

magics = list(map(int, input().split()))


def rotate(L):
    _board = [[0 for _ in range(2**N)] for _ in range(2**N)]
    r = 0
    while r < 2**N:
        c = 0
        while c < 2**N:
            nc = c + 2**L - 1
            for i in range(r, r + 2**L):
                nr = r
                for j in range(c, c + 2**L):
                    _board[nr][nc] = board[i][j]
                    nr += 1
                nc -= 1

            c += 2**L
        r += 2**L
    for i in range(2**N):
        for j in range(2**N):
            board[i][j] = _board[i][j]


def melt():
    global board
    mlt = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(2**N):
        for y in range(2**N):
            if board[x][y] == 0:
                continue
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 2**N or ny < 0 or ny >= 2**N:
                    continue
                if board[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                mlt.append([x, y])
    for x, y in mlt:
        board[x][y] -= 1


for L in magics:
    if L >= 1:
        rotate(L)
    melt()


def dfs(x, y, is_visited):
    global board
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = []
    stack.append([x, y])
    result = 0
    while stack:
        x, y = stack.pop()
        result += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 2**N or ny < 0 or ny >= 2**N:
                continue
            if is_visited[nx][ny] or board[nx][ny] == 0:
                continue
            is_visited[nx][ny] = True
            stack.append([nx, ny])

    return result


ans = 0
is_visited = [[False for _ in range(2**N)] for _ in range(2**N)]
max_size = 0
for x in range(2**N):
    for y in range(2**N):
        if board[x][y] > 0:
            ans += board[x][y]
            if not is_visited[x][y]:
                is_visited[x][y] = True
                max_size = max(max_size, dfs(x, y, is_visited))


print(ans)
print(max_size)
