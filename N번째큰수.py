import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  A = sorted(list(map(int, input().split())))
  print(A[-3])