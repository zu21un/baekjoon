import sys

input = sys.stdin.readline

N = int(input())

city = [[0 for _ in range(N + 1)]]

for _ in range(N):
    line = list(map(int, input().split()))
    city.append([0] + line)


def geri(x, y, d1, d2):
    sec = [0 for _ in range(6)]

    # 구역 1
    r = 1
    while r < x:
        sec[1] += sum(city[: y + 1])
        r += 1
    i = 1
    while r < x + d1:
        sec[1] += sum(city[: y + 1 - i])
        i += 1
        r += 1
    # 구역 2
    r = 1
    while r < x:
        sec[2] += sum(city[y + 1 :])
        r += 1
    i = 1
    while r < x + d2:
        sec[2] += sum(city[y + 1 + i :])
        i += 1
        r += 1
    # # 구역 3
    # r = x + d1
    # i = d2
    # while r < x + d1 + d2:
    #   sec[3] += sum(city[:y + 1])
    #   r += 1
    # i = 1
    # while r < x + d1:
    #   sec[3] += sum(city[:y + 1 - i])
    #   i += 1
    #   r += 1
    # # 구역 2
    # r = 1
    # while r < x:
    #   sec[2] += sum(city[y + 1:])
    #   r += 1
    # i = 1
    # while r < x + d2:
    #   sec[2] += sum(city[y + 1 + i:])
    #   i += 1
    #   r += 1

    return max(sec[1:]) - min(sec[1:])


# d1, d2 >= 1

# 1 <= x < x + d1 + d2 <= N
# d1 + d2 <= N - x

# 1 <= y - d1 < y < y + d2 <= N
# d1 <= y - 1
# d2 <= N - y

min_diff = float("inf")

for x in range(1, N + 1):
    for y in range(1, N + 1):
        d1 = 1
        while d1 <= y - 1:
            d2 = 1
            while d2 <= N - y and (d1 + d2) <= N - x:
                diff = geri(x, y, d1, d2)
                min_diff = min(diff, min_diff)
                d2 += 1
                continue
            d1 += 1

print(min_diff)
