n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
sum = 0
for i in a:
    n -= 1
    sum += i * b[n]
print(sum)