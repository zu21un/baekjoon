import sys
input = sys.stdin.readline

N = int(input())

schedules = []

for _ in range(N):
    schedule = list(map(int, input().split()))
    schedules.append(schedule)

schedules.sort(key=lambda x: (x[1], x[0]))

cnt = 0
meeting = [-1, -1]
for schedule in schedules:
    if schedule[0] >= meeting[1]:
        meeting = schedule
        cnt += 1

print(cnt)