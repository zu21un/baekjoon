cnt = int(input())
for i in range(cnt):
    a, b = map(int, input().split())
    len = b - a
    n = 1
    start = 0
    end = 0
    result = 0
    while True:
        end += n
        result += 1
        if len <= start + end:
            break
        start += n
        result += 1
        if len <= start + end:
            break
        n += 1
    print(result)