N = int(input())

plus_nums = []
minus_nums = []
has_zero = False
result = 0
for _ in range(N):
  num = int(input())
  if num == 1:
    result += 1
  elif num > 0:
    plus_nums.append(num)
  elif num < 0:
    minus_nums.append(num)
  elif num == 0:
    has_zero = True

if len(plus_nums) > 0:
  plus_nums.sort(reverse=True)
  if len(plus_nums) % 2 == 1:
    result += plus_nums[-1]
    plus_nums.pop()

  for i in range(0, len(plus_nums), 2):
    result += plus_nums[i] * plus_nums[i + 1]
    
if len(minus_nums) > 0:
  minus_nums.sort()
  
  if len(minus_nums) % 2 == 1:
    if not has_zero:
      result += minus_nums[-1]
    minus_nums.pop()

  for i in range(0, len(minus_nums), 2):
    result += minus_nums[i] * minus_nums[i + 1]

print(result)