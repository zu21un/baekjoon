from copy import deepcopy

import sys

input = sys.stdin.readline

dir_dict = {
    1: [-1, 0],
    2: [-1, -1],
    3: [0, -1],
    4: [1, -1],
    5: [1, 0],
    6: [1, 1],
    7: [0, 1],
    8: [-1, 1],
}

fish_dict = {}

board = []

# board: 물고기 번호, 방향
# fish_dict: 물고기 번호, 위치

for i in range(4):
    fish_info = list(map(int, input().split()))
    line = []
    for j in range(0, 7, 2):
        num, dir = fish_info[j], fish_info[j + 1]
        line.append([num, dir])
        fish_dict[num] = [i, j // 2]
    board.append(line)

SHARK = 99

fish, dir = board[0][0]
fish_dict[SHARK] = [0, 0]
del fish_dict[fish]
board[0][0][0] = SHARK
eat_fish = fish


def move_fish(fish_dict, board):
    for fish in range(1, 17):
        if fish not in fish_dict:
            continue
        r, c = fish_dict[fish]
        d = board[r][c][1]
        for _ in range(8):
            dr, dc = dir_dict[d]
            nr, nc = r + dr, c + dc
            if 0 <= nr < 4 and 0 <= nc < 4 and board[nr][nc][0] != SHARK:
                # change
                board[r][c][1] = d
                n_fish = board[nr][nc][0]
                board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                fish_dict[fish] = [nr, nc]
                fish_dict[n_fish] = [r, c]
                break
            d += 1
            if d > 8:
                d = 1

    return fish_dict, board


stack = []
stack.append([fish_dict, board, eat_fish])
max_eat_fish = 0
while stack:
    fish_dict, board, eat_fish = stack.pop()
    fish_dict, board = move_fish(fish_dict, board)
    shark_r, shark_c = fish_dict[SHARK]
    d = board[shark_r][shark_c][1]
    dr, dc = dir_dict[d]
    nr, nc = shark_r, shark_c

    can_eat = False
    while 0 <= nr + dr < 4 and 0 <= nc + dc < 4:
        nr += dr
        nc += dc
        if board[nr][nc][0] == 0:
            continue

        can_eat = True
        fish, dir = board[nr][nc]
        n_fish_dict = deepcopy(fish_dict)
        n_fish_dict[SHARK] = [nr, nc]
        del n_fish_dict[fish]
        n_board = deepcopy(board)
        n_board[shark_r][shark_c][0] = 0
        n_board[nr][nc][0] = SHARK
        n_eat_fish = eat_fish + fish
        stack.append([n_fish_dict, n_board, n_eat_fish])

    if not can_eat:
        max_eat_fish = max(max_eat_fish, eat_fish)

print(max_eat_fish)
