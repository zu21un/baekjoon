K = int(input())

stack = []
for _ in range(K):
  num = int(input())
  if stack and num == 0:
    stack.pop()
  else:
    stack.append(num)

print(sum(stack))