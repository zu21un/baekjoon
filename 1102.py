import math

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x2 - x1)**2 + (y2 - y1)**2
    d = math.sqrt(d)
    if d == 0:
        if r1 != r2:
            print(0)
        else:
            if r1 == 0:
                print(1)
            else:
                print(-1)
    else:
        nums = [d, r1, r2]
        nums.sort()
        if nums[0] + nums[1] == nums[2]:
            print(1)
        elif nums[0] + nums[1] < nums[2]:
            print(0)
        else:
            print(2)