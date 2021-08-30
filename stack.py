# https://www.acmicpc.net/problem/10828
import sys

arr = []
size = 0
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    cmd = list(sys.stdin.readline().rstrip().split())
    if cmd[0] == 'push':
        arr.append(int(cmd[1]))
        size += 1
    elif cmd[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(arr.pop())
            size -= 1
    elif cmd[0] == 'size':
        print(size)
    elif cmd[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if size == 0:
            print(-1)
        else:
            print(arr[size - 1])
        