import sys

T = int(sys.stdin.readline())
for i in range(1, T + 1) :
    A, B = map(int, sys.stdin.readline().split())
    print("Case #", i, ": ", (A + B), sep = "")