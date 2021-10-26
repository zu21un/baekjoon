T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    num = max(A, B)
    i = 1
    while True:
        if (num*i) % A == 0 and (num*i) % B == 0:
            print(num * i)
            break
        i += 1
    