# https://www.acmicpc.net/problem/10845

from collections import deque
import sys

N = int(input())
queue = deque()
for _ in range(N):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            pop = queue.popleft()
            print(pop)
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])