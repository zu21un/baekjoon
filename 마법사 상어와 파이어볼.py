from copy import deepcopy

N, M, K = map(int, input().split())

fireballs = []
dir_dict = {
    0: [-1, 0],
    1: [-1, 1],
    2: [0, 1],
    3: [1, 1],
    4: [1, 0],
    5: [1, -1],
    6: [0, -1],
    7: [-1, -1],
}

# r, c, m(질량), s(속력), d(방향)
for i in range(M):
    info = list(map(int, input().split()))
    info[0] -= 1
    info[1] -= 1
    fireballs.append(info)

for _ in range(K):
    # move
    board = [[[] for _ in range(N)] for _ in range(N)]
    for i, fireball in enumerate(fireballs):
        x, y, m, s, d = fireball
        dx, dy = dir_dict[d]
        nx, ny = (x + dx * s) % N, (y + dy * s) % N
        board[nx][ny].append(i)

    n_fireballs = []
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) == 0:
                continue
            if len(board[i][j]) == 1:
                idx = board[i][j][0]
                n_fireball = fireballs[idx]
                n_fireball[0] = i
                n_fireball[1] = j
                n_fireballs.append(n_fireball)
                continue
            total_m = 0
            total_s = 0
            total_d = 0
            for k in board[i][j]:
                x, y, m, s, d = fireballs[k]
                total_m += m
                total_s += s
                total_d += d % 2

            nm = total_m // 5
            if nm == 0:
                continue
            ns = total_s // len(board[i][j])
            nd = None
            if total_d == 0 or total_d == len(board[i][j]):
                nd = 0
            else:
                nd = 1
            for l in range(4):
                n_fireballs.append([i, j, nm, ns, nd])
                nd += 2
    fireballs = deepcopy(n_fireballs)
answer = 0
for fireball in fireballs:
    x, y, m, s, d = fireball
    answer += m

print(answer)
