import sys
n, m = map(int, sys.stdin.readline().split())
road = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
road.sort(key = lambda x : x[2])
root = [i for i in range(n+1)]
MAX = 0
def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]
def union(x, y):
    x = find(x)
    y = find(y)
    root[y] = x
connection = 1
cnt = 0
for a, b, c in road:
    if connection == n:
        break
    if find(a) != find(b):
        union(a, b)
        cnt += c
        MAX = max(MAX, c)
        connection += 1
    else:
        continue
print(cnt - MAX)