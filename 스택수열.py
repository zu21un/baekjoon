n = int(input())
arr = []
stack = []
pushed = 0
possible = True
for _ in range(n):
    num = int(input())
    if num > pushed:
        for _ in range(num - pushed):
            pushed += 1
            stack.append(pushed)
            arr.append("+")
        arr.append("-")
        stack.pop()
    else:
        poped = stack.pop()
        if num == poped:
            arr.append("-")
        else:
            possible = False
            break

if possible:
    for c in arr:
        print(c)
else:
    print("NO")


