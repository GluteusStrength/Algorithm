import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        root[y] = x
        friend[x] += friend[y]
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    root = defaultdict(str)
    friend = defaultdict(int)
    for i in range(m):
        a, b = sys.stdin.readline().split()
        if a not in friend:
            root[a] = a
            friend[a] = 1
        if b not in friend:
            root[b] = b
            friend[b] = 1
        union(a, b)
        print(friend[root[a]])