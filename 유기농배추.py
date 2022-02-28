import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0 for i in range(M)] for j in range(N)]

    for _ in range(K):
        col, row = map(int, input().split())
        field[row][col] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                stack = [(i, j)]
                while stack:
                    row, col = stack.pop()
                    field[row][col] = 0
                    if row - 1 >= 0 and field[row - 1][col] == 1:
                        stack.append((row - 1, col))
                    if row + 1 < N and field[row + 1][col] == 1:
                        stack.append((row + 1, col))
                    if col - 1 >= 0 and field[row][col - 1] == 1:
                        stack.append((row, col - 1))
                    if col + 1 < M and field[row][col + 1] == 1:
                        stack.append((row, col + 1))
                answer += 1
    print(answer)
        