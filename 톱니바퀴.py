import sys

input = sys.stdin.readline

gears = []
for _ in range(4):
    gear = list(input().rstrip())
    gears.append(list(map(int, gear)))

# 각 항의 첫번째 값이 left, 두번째 항이 right
gear_info = [[6, 2] for _ in range(4)]

K = int(input())


def rotate(cur_num, dir):
    for i in range(2):
        gear_info[cur_num][i] = (gear_info[cur_num][i] - dir) % 8


def is_rotate_next(b, n):
    b_gear = gears[b]
    n_gear = gears[n]
    b_left, b_right = gear_info[b]
    n_left, n_right = gear_info[n]

    if n < b and n_gear[n_right] != b_gear[b_left]:
        return True
    elif n > b and n_gear[n_left] != b_gear[b_right]:
        return True

    return False


def rotate_next(b, c, dir):
    n = c + (c - b)
    if 0 <= n < 4 and is_rotate_next(c, n):
        rotate_next(c, n, -dir)
    rotate(c, dir)


for _ in range(K):
    gear_num, dir = map(int, input().split())
    gear_num -= 1

    if gear_num > 0 and is_rotate_next(gear_num, gear_num - 1):
        rotate_next(gear_num, gear_num - 1, -dir)
    if gear_num < 3 and is_rotate_next(gear_num, gear_num + 1):
        rotate_next(gear_num, gear_num + 1, -dir)
    rotate(gear_num, dir)

answer = 0
for gear_num in range(4):
    gear_top = (gear_info[gear_num][0] + 2) % 8
    gear = gears[gear_num]
    answer += gear[gear_top] * (2**gear_num)

print(answer)
