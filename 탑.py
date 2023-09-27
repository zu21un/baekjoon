import sys
input = sys.stdin.readline

N = int(input())

towers = list(map(int, input().split()))
towers_with_index = []
for idx, value in enumerate(towers):
  towers_with_index.append((value, idx))
towers_with_index.sort(key=lambda x: -x[0])
print(towers_with_index)

answer = [-1 for _ in range(N)]

left = right = towers_with_index[0][1]
answer[towers_with_index[0][1]] = 0

for value, idx in towers_with_index:
  if idx < left:
    answer[idx] = 0
    left = idx
  elif idx > right:
    answer[idx] = right + 1
    right = idx
  else:
    for i in range(idx-1, left-1, -1):
      if answer[i] != -1:
        answer[idx] = i + 1
        break

print(answer)