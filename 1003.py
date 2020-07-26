zero = [1, 0]
one = [0, 1]
arr = []
max = -1
n = int(input())
for i in range(n):
    num = int(input())
    arr.append(num)
    if num > max:
        max = num
for i in range(2, max + 1):
    zero.append(zero[i - 1] + zero[i - 2])
    one.append(one[i - 1] + one[i - 2])
for i in arr:
    print(zero[i], one[i])

    
