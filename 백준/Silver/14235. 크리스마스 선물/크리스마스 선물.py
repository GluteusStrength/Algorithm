import sys, heapq
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    p = list(map(int, sys.stdin.readline().split()))
    if len(p) == 1:
        if not heap:
            print(-1)
        else:
            print(-heapq.heappop(heap))
    else:
        for j in p[1:]:
            heapq.heappush(heap, -j)