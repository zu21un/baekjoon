N, M = map(int, input().split())
for i in range(min(N, M), 0, -1):
    if N % i == 0 and M % i == 0:
        print(i)
        break
num = max(N, M)
i = 1
while True:
    if (num * i) % N == 0 and (num * i) % M == 0:
        print(num * i)
        break
    i += 1