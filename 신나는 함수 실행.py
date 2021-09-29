# https://www.acmicpc.net/problem/9184

memo = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
memo[0][0][0] = 1
def funfunc(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return memo[0][0][0]
    if a > 20 or b > 20 or c > 20:
        if memo[20][20][20] == 0:
            memo[20][20][20] = funfunc(20, 20, 20)
        return memo[20][20][20]
    if a < b and b < c:
        if memo[a][b][c - 1] == 0:
            memo[a][b][c - 1] = funfunc(a, b, c - 1)
        if memo[a][b - 1][c - 1] == 0:
            memo[a][b - 1][c - 1] = funfunc(a, b - 1, c - 1)
        if memo[a][b - 1][c] == 0:
            memo[a][b - 1][c]= funfunc(a, b - 1, c)
        return memo[a][b][c - 1] + memo[a][b - 1][c - 1] - memo[a][b - 1][c]
    else:
        if memo[a - 1][b][c] == 0:
            memo[a - 1][b][c] = funfunc(a - 1, b, c)
        if memo[a - 1][b - 1][c] == 0:
            memo[a - 1][b - 1][c] = funfunc(a - 1, b - 1, c)
        if memo[a - 1][b][c - 1] == 0:
            memo[a - 1][b][c - 1]= funfunc(a - 1, b, c - 1)
        if memo[a - 1][b - 1][c - 1] == 0:
            memo[a - 1][b - 1][c - 1] = funfunc(a - 1, b - 1, c - 1)
        return memo[a - 1][b][c] + memo[a - 1][b - 1][c] + memo[a - 1][b][c - 1] - memo[a - 1][b - 1][c - 1]
            


while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    result = funfunc(a, b, c)
    print(f'w({a}, {b}, {c}) = {result}')
