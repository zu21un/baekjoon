import sys
input = sys.stdin.readline

from heapq import heappush, heappop

N = int(input())
heap = []
classes = []

for _ in range(N):
  S, T = map(int, input().split())
  heappush(heap, (S, T))

while heap:
  start_time, end_time = heappop(heap)
  for idx, class_end_time in enumerate(classes):
    if class_end_time <= start_time:
      classes[idx] = end_time
      break
  else:
    classes.append(end_time)


  # need_new_class = True
  # while heap1:
  #   end_time = heappop(heap1)[1]
  #   if end_time <= S:
  #     heappush(heap2, (-T, T))
  #     need_new_class = False
  #   else:
  #     heappush(heap2, (-end_time, end_time))
  # if need_new_class:
  #   heappush(heap2, (-T, T))
    
  # heap1 = heap2[:]
  # heap2 = []

print(len(classes))