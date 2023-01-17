import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
jew = []
bag = []
for i in range(n):
    jew.append(list(map(int, sys.stdin.readline().split())))
for i in range(k):
    bag.append(int(sys.stdin.readline()))
jew.sort()
bag.sort()
heap = []
ans = 0
cnt = 0
for i in bag:
    m = i
    while jew and m >= jew[0][0]:
        heapq.heappush(heap, -jew[0][1])
        heapq.heappop(jew)
    if heap:
        ans += heapq.heappop(heap)
        cnt += 1
    elif not jew:
        break
print(-ans)