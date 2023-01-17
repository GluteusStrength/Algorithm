import sys
import heapq
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))
for _ in range(n):
    print(heapq.heappop(heap))

