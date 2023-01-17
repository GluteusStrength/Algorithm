import heapq
import sys
n = int(input())
heap = []
c = []
for i in range(n):
    c.append(list(map(int,sys.stdin.readline().split())))
c = sorted(c, key = lambda x : x[1])
heapq.heappush(heap, c[0][2])
for i in range(1, n):
    flag = c[i][1]
    if flag >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, c[i][2])
    else:
        heapq.heappush(heap, c[i][2])
print(len(heap))