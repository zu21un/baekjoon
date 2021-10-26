import heapq
import sys

N = int(input())

left = []
right = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if left == []:
        print(num)
        heapq.heappush(left, -num)
    elif right == []:
        if num < -left[0]:
            print(num)
            heapq.heappush(right, -heapq.heappop(left))
            heapq.heappush(left, -num)
        else:
            print(-left[0])
            heapq.heappush(right, num)            
    else:
        if len(left) > len(right):
            if -left[0] < num:
                heapq.heappush(right, num)
            else:
                heapq.heappush(right, -heapq.heappop(left))
                heapq.heappush(left, -num)
        else:
            if num < right[0]:
                heapq.heappush(left, -num)
            else:
                heapq.heappush(left, -heapq.heappop(right))
                heapq.heappush(right, num)
        print(-left[0])




