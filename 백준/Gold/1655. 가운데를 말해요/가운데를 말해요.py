import sys
import heapq
n = int(sys.stdin.readline())
l_heap = []
r_heap = []
for i in range(n):
    t = int(sys.stdin.readline())
    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, -t)
    else:
        heapq.heappush(r_heap, t)
    if len(l_heap) >= 1 and len(r_heap) >= 1:
        if r_heap[0] < (l_heap[0] * -1):
            x = heapq.heappop(l_heap)
            y = heapq.heappop(r_heap)
            heapq.heappush(l_heap, -y)
            heapq.heappush(r_heap, -x)
    print(l_heap[0] * -1)




