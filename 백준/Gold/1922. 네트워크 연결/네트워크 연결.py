import sys
v = int(input())
e = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]
graph.sort(key = lambda x : x[2])
root = [i for i in range(v+1)]
def find(x):
    if root[x] == x:
        return x
    return find(root[x])
res = 0
for s, e, w in graph:
    x = find(s)
    y = find(e)
    if x != y:
        res += w
        root[y] = x
print(res)