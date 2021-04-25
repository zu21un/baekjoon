while True:
    A, B, C = map(int, input().split())
    if A==B==C==0:
        break
    else:
        lines = [A, B, C]
        lines.sort()
        if lines[0]*lines[0] + lines[1]*lines[1] == lines[2]*lines[2]:
            print('right')
        else:
            print('wrong')