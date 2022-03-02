import sys

input = sys.stdin.readline

def check(board, N, L):
    answer = 0
    for line in board:
        cont = 1
        for i, (a, b) in enumerate(zip(line, line[1:])):
            if a == b:
                cont += 1
            elif a < b:
                if a + 1 == b and cont >= L:
                    cont = 1
                    continue
                else:
                    break
            elif a > b:
                if a == b + 1:
                    is_continue = True
                    for j in range(i + 2, i + L + 1):
                        if j >= N or line[j] != b:
                            is_continue = False
                            break
                    else:
                        cont = -L + 1
                        continue
                    if not is_continue:
                        break
                else:
                    break
        else:
            answer += 1
            # print(line)
            
    return answer

N, L = map(int, input().split())

board = []
for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    

new_board = [[0 for _ in range(N)] for _ in range(N)]

for i, line in enumerate(board):
    for j, v in enumerate(line):
        new_board[i][j] = board[j][i]

# print("board")
answer = check(board, N, L)
# print("new_board")
answer += check(new_board, N, L)
print(answer)

