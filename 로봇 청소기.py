N, M = map(int, input().split())


r, c, d = map(int, input().split())

dir_dict = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

answer = 0

while True:
    if room[r][c] == 0:
        room[r][c] = -1
        answer += 1

    for i in range(1, 5):
        rotated_dir = (d - i) % 4
        dx, dy = dir_dict[rotated_dir]

        if 0 <= r + dx < N and 0 <= c + dy < M and room[r + dx][c + dy] == 0:
            r += dx
            c += dy
            d = rotated_dir
            break
    else:
        dx, dy = dir_dict[d]
        if room[r - dx][c - dy] != 1:
            r -= dx
            c -= dy
        else:
            break

print(answer)
