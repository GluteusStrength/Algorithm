import sys, heapq
n = int(sys.stdin.readline())
gas = []
for _ in range(n):
    heapq.heappush(gas, list(map(int, sys.stdin.readline().split())))
l, p = map(int, sys.stdin.readline().split())
heap = []
cnt = 0
while p < l:
    while gas and gas[0][0] <= p:
        x, y = heapq.heappop(gas)
        heapq.heappush(heap, [-y, x])
    if not heap: # 해당 주유소 없으면?
        cnt = -1
        break
    f, m = heapq.heappop(heap)
    p += -f
    cnt += 1
print(cnt)
