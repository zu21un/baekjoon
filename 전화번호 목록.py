import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  phone_num_list = []
  for _ in range(n):
    phone_num = input().rstrip()
    phone_num_list.append(phone_num)
  phone_num_list.sort()
  for i in range(n - 1):
    if phone_num_list[i + 1].startswith(phone_num_list[i]):
      print('NO')
      break
  else:
    print('YES')
    
  
  
