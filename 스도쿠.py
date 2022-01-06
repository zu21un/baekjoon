import sys
input = sys.stdin.readline

global board

board = []

for i in range(9):
    line = list(map(int, input().split()))
    board.append(line)
    
def ispossible(row, col, num):
    global board
    
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    for i in range((row // 3) * 3, (row // 3) * 3 + 3):
        for j in range((col // 3) * 3, (col // 3) * 3 + 3):
            if board[i][j] == num:
                return False
    return True
            
def sudoku(row, col):
    global board

    if row == 9:
        return True
    elif board[row][col] == 0:
        for i in range(1,10):
            if ispossible(row, col, i):
                board[row][col] = i
                if sudoku(row + ((col + 1) // 9), (col + 1) % 9):
                    return True
                else:
                    board[row][col] = 0
        return False
    else:
        return sudoku(row + ((col + 1) // 9), (col + 1) % 9)

sudoku(0,0)
for row in board:
    line = ' '.join(map(str, row))
    print(line)



  


# while stack:
#     sudoku = stack.pop()
    
#     else:
#         for line in sudoku:
#             nums = ' '.join(map(str, line))
#             print(nums)
#         break
    