import sys
import heapq
n = int(sys.stdin.readline())
task = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
heap = [] # 최대힙을 만들어준다.
m = 0
for i in task:
    x = [-i[1], i[0]]
    m = max(m, i[0])
    heapq.heappush(heap, x)
dp = [0 for _ in range(m+1)]
while heap:
    flag = heapq.heappop(heap)
    for i in range(flag[1], 0, -1):
        if dp[i] == 0:
            dp[i] = flag[0]
            break
print(-sum(dp))
