import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
work = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
in_degree = [0 for _ in range(n+1)]
w = [[] for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
time = [0]
for i in range(1, n+1):
    time.append(work[i-1][0])
    dp[i] = time[i]
    if i == 1:
        dp[i] = work[i-1][0]
    if work[i-1][1] != 0:
        x = work[i-1][2:]
        for j in x:
            in_degree[i] += 1
            w[j].append(i)
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)
while queue:
    cur = queue.popleft() # 해당 작업을 수행한다는 의미.
    for i in w[cur]:
        in_degree[i] -= 1
        dp[i] = max(dp[cur]+time[i], dp[i])
        if in_degree[i] == 0: # 선행되어야 할 작업이 모두 마무리 되었다면?
            queue.append(i)

print(max(dp))
