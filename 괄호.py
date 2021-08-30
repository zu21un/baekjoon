# https://www.acmicpc.net/problem/9012

import sys

T = int(input())
for _ in range(T):
    S = sys.stdin.readline().rstrip()
    isVPS = 0
    stack = 0
    for c in S:
        if c == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            isVPS = -1
            break
    if isVPS == 0 and stack == 0:
        print("YES")
    else:
        print("NO")
    