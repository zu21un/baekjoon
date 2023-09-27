BLACK = -1
RAINBOW = 0
EMPTY = -2
rainbow_list = []

N, M = map(int, input().split())
board = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == RAINBOW:
            rainbow_list.append([i, j])
    board.append(line)

point = 0
