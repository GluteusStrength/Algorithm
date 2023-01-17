import sys
import heapq
n = int(sys.stdin.readline())
c = []
heap = []
for i in range(n):
    c.append(list(map(int, sys.stdin.readline().split())))
c.sort()
heapq.heappush(heap, c[0][1])
for i in range(1, n):
    x = c[i]
    if heap[0] > x[0]:
        heapq.heappush(heap, x[1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, x[1])
print(len(heap))

