import sys
input = sys.stdin.readline

current = max_people = 0

for _ in range(10):
  get_out, get_in = map(int, input().split())
  current -= get_out
  current += get_in
  max_people = max(current, max_people)

print(max_people)