import sys, heapq
n, m = map(int, sys.stdin.readline().split())
heap = []
cnt = 0
for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    Class = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(Class)
    if p < l:
        heapq.heappush(heap,1)
    else:
        k = 0
        for i in range(p-l+1):
            k = heapq.heappop(Class)
        heapq.heappush(heap, k)
res = 0
while heap:
    res += heapq.heappop(heap)
    if res > m:
        break
    else:
        cnt += 1
print(cnt)
