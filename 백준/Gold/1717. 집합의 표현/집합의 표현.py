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

for i in range(m):
    o, a, b = map(int, sys.stdin.readline().split())
    if o == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")