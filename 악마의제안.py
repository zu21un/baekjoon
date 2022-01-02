import sys
input = sys.stdin.readline

K, N = map(int,input().split())

if N == 1:
     print(-1)
else:
    X = (N//(N-1)) * K
    while (X - K)*N < X:
        X += 1
    print(X)

