N, K = map(int, input().split())

objs = []

max_value = 0
for _ in range(N):
    objs.append(list(map(int, input().split())))

idx = 0
value = 0
weight = 0

stack = []
stack.append([idx, value, weight])

while stack:
    idx, value, weight = stack.pop()
    if weight > K:
        continue
    max_value = max(max_value, value)
    if idx < N:
        _weight, _value = objs[idx][0], objs[idx][1]
        idx += 1
        stack.append([idx, value, weight])
        stack.append([idx, value + _value, weight + _weight])

print(max_value)
