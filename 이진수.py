import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  n = int(input())
  num = 0
  while n > 0:
    if n % 2 == 1:
      print(f'{num} ', end='')
    num += 1
    n = n >> 1

