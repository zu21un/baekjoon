# https://www.acmicpc.net/problem/1158

N, K = map(int, input().split())
arr = [n for n in range(1, N + 1)]
idx = K - 1
size = N
print("<", end="")
for _ in range(N - 1):
    print("%d, "%arr[idx], end="")
    del arr[idx]
    size -= 1
    idx += K - 1
    idx %= size
print("%d>"%arr[0])

