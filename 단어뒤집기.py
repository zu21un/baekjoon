# https://www.acmicpc.net/problem/9093
import sys

T = int(input())
for _ in range(T):
    words = list(sys.stdin.readline().split())
    for word in words:
        print(word[::-1], end=' ')
    print()
    