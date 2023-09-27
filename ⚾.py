import sys
input = sys.stdin.readline
from collections import defaultdict
from itertools import permutations

N = int(input())

players = defaultdict(list)
for _ in range(N):
  players_score = list(map(int, input().split()))
  for idx, score in enumerate(players_score):
    players[idx + 1].append(score)

max_score = 0
players_without_1 = [2,3,4,5,6,7,8,9]
players_without_1 = list(permutations(players_without_1))

for player_order_without_1 in players_without_1:
  player_order_without_1 = list(player_order_without_1)
  player_order = player_order_without_1[:3] + [1] + player_order_without_1[3:]

  next_player_idx = 0
  score = 0
  for ining in range(N):
    out_score = 0
    ground = [False, False, False]
    while out_score < 3:
      result = players[player_order[next_player_idx]][ining]
      
      if result == 0:
        out_score += 1
      else:
        next_ground = [False] * (result - 1) + [True]
        ground = next_ground + ground
        for player in ground[3:]:
          if player == True:
            score += 1
        ground = ground[:3]
      
      next_player_idx = (next_player_idx + 1) % 9
  max_score = max(score, max_score)

print(max_score)