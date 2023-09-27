import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

dice = [[0 for _ in range(3)] for _ in range(4)]
# 1,1 = center
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

cmds = list(map(int, input().split()))

cmd_dict = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}


def roll(dx, dy):
    if dx == 0:
        dice[3][1], dice[1][1 + dy] = dice[1][1 + dy], dice[3][1]
        (dice[1][(0 + dy) % 3], dice[1][(1 + dy) % 3], dice[1][(2 + dy) % 3]) = (
            dice[1][0],
            dice[1][1],
            dice[1][2],
        )
    else:
        (
            dice[(0 + dx) % 4][1],
            dice[(1 + dx) % 4][1],
            dice[(2 + dx) % 4][1],
            dice[(3 + dx) % 4][1],
        ) = (
            dice[0][1],
            dice[1][1],
            dice[2][1],
            dice[3][1],
        )


for cmd in cmds:
    dx, dy = cmd_dict[cmd]
    nx = x + dx
    ny = y + dy
    if 0 > nx or N <= nx or 0 > ny or M <= ny:
        continue

    roll(dx, dy)

    x, y = nx, ny
    if board[x][y] == 0:
        board[x][y] = dice[3][1]
    else:
        dice[3][1], board[x][y] = board[x][y], 0

    print(dice[1][1])
