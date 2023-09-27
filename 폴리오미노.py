import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = 0


def search(tetro):
    max_sum = 0
    w, h = len(tetro), len(tetro[0])
    for w_s in range(0, N - w + 1):
        for h_s in range(0, M - h + 1):
            tmp = 0
            for r in range(w):
                for c in range(h):
                    if tetro[r][c] == 1:
                        tmp += board[w_s + r][h_s + c]
            max_sum = max(max_sum, tmp)

    return max_sum


def rotate(tetro):
    return list(map(list, zip(*tetro[::-1])))


def reverse_h(tetro):
    reverse_tetro = []
    for t in tetro:
        reverse_tetro.append(t[::-1])

    return reverse_tetro


def reverse_v(tetro):
    return tetro[::-1]


tetros = []
tetro_1 = [[1, 1, 1, 1]]
tetro_2 = [[1, 1], [1, 1]]
tetro_3 = [[1, 0], [1, 0], [1, 1]]
tetro_4 = [[1, 0], [1, 1], [0, 1]]
tetro_5 = [[1, 1, 1], [0, 1, 0]]

tetros.append(tetro_1)
tetros.append(rotate(tetro_1))
tetros.append(tetro_2)

for _ in range(4):
    tetros.append(tetro_3)
    tetro_3 = rotate(tetro_3)

tetro_3 = reverse_v(tetro_3)
for _ in range(4):
    tetros.append(tetro_3)
    tetro_3 = rotate(tetro_3)

for _ in range(2):
    tetros.append(tetro_4)
    tetro_4 = rotate(tetro_4)

tetro_4 = reverse_v(tetro_4)
for _ in range(2):
    tetros.append(tetro_4)
    tetro_4 = rotate(tetro_4)

for _ in range(4):
    tetros.append(tetro_5)
    tetro_5 = rotate(tetro_5)

for tetro in tetros:
    answer = max(answer, search(tetro))

print(answer)
