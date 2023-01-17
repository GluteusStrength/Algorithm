import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
root = [i for i in range(n+1)]
def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        root[y] = x
    else:
        root[x] = y

flag = False
cnt = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    cnt += 1
    if find(a) != find(b):
        union(a, b)
        continue
    if find(a) == find(b):
        flag = True
        break
if flag:
    print(cnt)
else:
    print(0)