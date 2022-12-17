import sys
from itertools import combinations
input = sys.stdin.readline

dwarfs = []
for _ in range(9):
  dwarfs.append(int(input()))

dwarfs.sort()
sum_height = sum(dwarfs)

over_height = sum_height - 100

for a, b in combinations(dwarfs, 2):
  if a + b == over_height:
    dwarfs.remove(a)
    dwarfs.remove(b)
    break

for dwarf in dwarfs:
  print(dwarf)
