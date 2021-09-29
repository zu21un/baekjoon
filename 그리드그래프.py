T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    print(1)
    print('(0,0)')
    for a in range(0, m):
        if a % 2 == 0:
            for b in range(1, n):
                print(f'({a},{b})')
        else:
            for b in range(n - 1, 0, -1):
                print(f'({a},{b})')
    for x in range(a, 0, -1):
        print(f'({x},0)')