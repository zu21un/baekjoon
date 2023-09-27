import sys

input = sys.stdin.readline

dir_dict = {
    0: [1, 0],
    1: [0, -1],
    2: [-1, 0],
    3: [0, 1],
}

board = [[False for _ in range(101)] for _ in range(101)]

N = int(input())

stack = []


def check():
    cnt = 0
    for i in range(100):
        for j in range(100):
            if (
                board[i][j]
                and board[i + 1][j]
                and board[i][j + 1]
                and board[i + 1][j + 1]
            ):
                cnt += 1
    return cnt


for _ in range(N):
    x, y, d, g = map(int, input().split())
    stack = [d]

    for i in range(g):
        l = len(stack)
        for j in range(l - 1, -1, -1):
            stack.append((stack[j] + 1) % 4)

    board[x][y] = True
    for s in stack:
        dx, dy = dir_dict[s]
        x += dx
        y += dy
        board[x][y] = True

answer = check()

print(answer)
