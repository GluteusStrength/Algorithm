import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
in_degree = [0 for _ in range(n+1)]
order = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
order.sort(key = lambda x : x[0], reverse = True)
queue = deque()
for i in order:
    flag = i[1:]
    for j in range(1, len(flag)):
        in_degree[flag[j]] += 1
        graph[flag[j-1]].append(flag[j])
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)
res = []
while queue:
    s = queue.popleft()
    res.append(s)
    for i in graph[s]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)
if len(res) == n:
    for i in res:
        print(i)
else:
    print(0)