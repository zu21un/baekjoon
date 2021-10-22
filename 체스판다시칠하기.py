N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())

min = float('inf')

for i in range(7, N):
    tmp_board = board[i-7:i+1]
    for j in range(7, M):
        #case 1
        result = 0
        for line_num, line in enumerate(tmp_board):
            tmp_line = line[j - 7: j + 1]
            for idx, c in enumerate(tmp_line):
                if (line_num + idx)%2 == 0 and c != 'B':
                    result += 1
                if (line_num + idx)%2 == 1 and c != 'W':
                    result += 1
        if result < min:
            min = result
        #case 2
        result = 0
        for line_num, line in enumerate(tmp_board):
            tmp_line = line[j - 7: j + 1]
            for idx, c in enumerate(tmp_line):
                if (line_num + idx)%2 == 0 and c != 'W':
                    result += 1
                if (line_num + idx)%2 == 1 and c != 'B':
                    result += 1
        if result < min:
            min = result

print(min)

        
