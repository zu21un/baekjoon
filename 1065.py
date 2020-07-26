N = int(input())
num = 100
cnt = 99
if N < num:
    print(N)
else:
    while num <= N:
        a = num // 100
        b = (num % 100) // 10
        c = num % 10
        if a - b == b - c:
            cnt += 1
        num += 1
    print(cnt)
