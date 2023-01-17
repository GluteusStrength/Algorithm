import sys
# kruskal로 진행한다
# find 알고리즘
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]
# union 알고리즘
# parent 설정
def union(x, y):
    x = find(x)
    y = find(y)
    if y < x:
        root[x] = y
    else:
        root[y] = x
while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break
    total = 0
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    graph.sort(key=lambda x : x[2])
    root = [i for i in range(m)]
    for edge in graph:
        # root가 다르다면
        a, b, c = edge
        if find(a) != find(b):
            union(a, b)
        else:
            total += c
    print(total)
