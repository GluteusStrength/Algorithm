import sys, heapq
n, m = map(int, sys.stdin.readline().split())
in_degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
queue = []
prob = []
for _ in range(m):
    heapq.heappush(prob, list(map(int, sys.stdin.readline().split())))
for i in range(1, m+1):
    in_degree[prob[i-1][1]] += 1
    graph[prob[i-1][0]].append(prob[i-1][1])
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(queue, i)
res = []
while queue:
    cur = heapq.heappop(queue)
    res.append(cur)
    for i in graph[cur]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heapq.heappush(queue,i) # 작은 번호가 우선적으로 처리하게 끔 한다.
print(*res)