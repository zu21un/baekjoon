N = int(input())

stack = []
stack.append([0] * N)
count = 0
while stack:
    board = stack.pop()
    if 0 in board:
        queen = board.index(0)
        for i in range(1, N+1):
            new_board = board[:]
            new_board[queen] = i
            for j in range(queen):
                if new_board[j] == new_board[queen] or abs(new_board[queen] - new_board[j]) == queen - j:
                    break
            else:
                stack.append(new_board)
    else:
        count += 1
print(count)