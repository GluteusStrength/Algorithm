import sys, math
n = int(sys.stdin.readline())
x_co = []
y_co = []
z_co = []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    x_co.append((x, i))
    y_co.append((y, i))
    z_co.append((z, i))
x_co.sort()
y_co.sort()
z_co.sort()
root = [i for i in range(n)]
dist = []
for i in range(1, n): # x부터 확인한다.
    a = x_co[i]
    b = x_co[i-1]
    dist.append((a[0] - b[0], a[1], b[1]))
for i in range(1, n): # y 확인한다.
    a = y_co[i]
    b = y_co[i-1]
    dist.append((a[0] - b[0], a[1], b[1]))
for i in range(1, n): # z 확인한다.
    a = z_co[i]
    b = z_co[i-1]
    dist.append((a[0] - b[0], a[1], b[1]))
dist.sort()
def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]
def union(x, y):
    x = find(x)
    y = find(y)
    root[y] = x
res = 0
cnt = 0
for d, i, j in dist:
    if cnt == n-1:
        break
    if find(i) != find(j):
        union(i,j)
        cnt += 1
        res += d
print(res)
