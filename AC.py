from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    nums = input()
    nums = nums[1:-1].split(',')
    if nums[0] == '':
        nums = []
    else:
        nums = list(map(int, nums))
    nums = deque(nums)

    front = 'left'
    for c in p:
        if c == 'R':
            if front == 'left':
                front = 'right'
            else:
                front = 'left'
        elif c == 'D':
            if len(nums) == 0:
                print('error')
                break
            else:
                if front == 'left':
                    nums.popleft()
                else:
                    nums.pop()
    else:
        if front == 'right':
            nums.reverse()
        result = ','.join(map(str, list(nums)))
        print(f"[{result}]")

