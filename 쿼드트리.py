import sys
input = sys.stdin.readline

def quadtree(board):
    cnt = 0
    for line in board:
        cnt += sum(line)
        
    if cnt == 0:
        return '0'
    elif cnt == len(board)**2:
        return '1'
    else:
        result = '('
        board1, board2, board3, board4 = [], [], [], []
        for i in range(len(board)//2):
            board1.append(board[i][:len(board)//2])
            board2.append(board[i][len(board)//2:])
            board3.append(board[i + len(board)//2][:len(board)//2])
            board4.append(board[i + len(board)//2][len(board)//2:])
        result += quadtree(board1)
        result += quadtree(board2)
        result += quadtree(board3)
        result += quadtree(board4)
        
        result += ')'
        return result
    
N = int(input())
board = []
for _ in range(N):
    line = list(map(int, input().rstrip()))
    board.append(line)

print(quadtree(board))