N, M = map(int, input().split())
# 24 * N 시간

a = list(map(int, input().split()))
b = list(map(int, input().split()))
scores = []
for score in zip(a, b):
    scores.append(score)
scores.sort(key=lambda x: -x[1])
# print(scores)
N *= 24
for base, num in scores:
    time = (100-base) // num
    



