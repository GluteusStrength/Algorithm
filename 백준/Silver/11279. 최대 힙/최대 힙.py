import heapq
import sys
n = int(input())
heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            ans = heapq.heappop(heap)
            print(-ans)
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)