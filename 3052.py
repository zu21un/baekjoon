arr = []
for i in range(10):
    arr.append(int(input()) % 42)
nums = set(arr)
print(len(nums))
