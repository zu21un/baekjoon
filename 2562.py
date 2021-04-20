arr = []
for i in range(9):
    arr.append(int(input()))

maxnum = max(arr)
print(maxnum, arr.index(maxnum) + 1, sep = '\n')