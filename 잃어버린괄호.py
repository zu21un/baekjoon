s = input()
nums = list(map(int, s[:].replace('-', '+').split('+')))

ops = ['+']
for c in s:
    if c == '+' or c == '-':
        ops.append(c)
minus = False
for idx, op in enumerate(ops):
    if op == '-':
        if minus == False:
            minus = True
    if op == '+':
        if minus == True:
            ops[idx] = '-'
for idx, op in enumerate(ops):
    if op == '-':
        nums[idx] = -nums[idx]

print(sum(nums))




