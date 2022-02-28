import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board += list(input().rstrip())

answer = []

while '1' in board:
    find_home = board.index('1')
    stack = [find_home]
    cnt = 0
    while stack:
        home = stack.pop()
        
        if board[home] == '1':
            board[home] = '0'
            cnt += 1
            
        if ((home - 1) // N) == (home // N) and board[home - 1] == '1':
            stack.append(home - 1)
        if ((home + 1) // N) == (home // N) and board[home + 1] == '1':
            stack.append(home + 1)
        if home - N >= 0 and board[home - N] == '1':
            stack.append(home - N)
        if home + N < N*N and board[home + N] == '1':
            stack.append(home + N)
    answer.append(cnt)
    
answer.sort()
print(len(answer))
for a in answer:
    print(a)