import sys

input = sys.stdin.readline

N, K = map(int, input().split())
Belt = list(map(int, input().split()))
Robots = [False for i in range(2 * N)]


failed = 0

# Robots[0] = True
# Belt[0] -= 1
# if Belt[0] == 0:
#   failed += 1
level = 0

while failed < K:
  breakpoint()
  for i in range(2*N - 1, -1, -1):
    current, next = i % (2*N), (i+1) % (2*N)
    # breakpoint()
    if Robots[current] is False:
      continue

    if Robots[next] is False and Belt[next] >= 1:
      Robots[current] = False
      Belt[next] -= 1
      if next != 0:
        Robots[next] = True
      
      if Belt[next] == 0:
        failed += 1
        
  if Robots[0] is False and Belt[0] >= 1:
    Robots[0] = True
    Belt[0] -= 1
    
    if Belt[0] == 0:
      failed += 1
    
  
  level += 1

print(level)