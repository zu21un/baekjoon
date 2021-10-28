from collections import deque

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

min, max = float('inf'), -float('inf')
queue = deque()
cnt = 0

for i in range(4):
    if ops[i] > 0:
        new_ops = ops[:]
        new_ops[i] -= 1
        if i == 0:
            new_ops.append('+')
        elif i == 1:
            new_ops.append('-')
        elif i == 2:
            new_ops.append('*')
        elif i == 3:
            new_ops.append('/')
        queue.append(new_ops)

while queue:
    ops = queue.popleft()
    if sum(ops[:-1]) == 0:
        cnt += 1
        result = nums[0]
        for num, op in zip(nums[1:], ops[4]):
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            elif op == '*':
                result *= num
            elif op == '/':
                if result < 0:
                    result = -result
                    result //= num
                    result = -result
                else:
                    result //= num
                    
        if result > max:
            max = result
        if result < min:
            min = result
    else:
        for i in range(4):
            if ops[i] > 0:
                new_ops = ops[:]
                new_ops[i] -= 1
                if i == 0:
                    new_ops[4] += '+'
                elif i == 1:
                    new_ops[4] += '-'
                elif i == 2:
                    new_ops[4] += '*'
                elif i == 3:
                    new_ops[4] += '/'
                queue.append(new_ops)
print(max)
print(min)





