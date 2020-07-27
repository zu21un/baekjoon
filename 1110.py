N = int(input())
cnt = 0
num = N
while True:
    cnt += 1
    left = num // 10
    right = num % 10
    num = right * 10 + (left + right) % 10
    if num == N:
        break
print(cnt)