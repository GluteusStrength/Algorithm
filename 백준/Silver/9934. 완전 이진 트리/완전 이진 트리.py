import sys
k = int(input())
node = list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(k)]
def maketree(N, idx):
    mid = len(N)//2
    tree[idx].append(N[mid])
    if len(N) == 1:
        return 0
    maketree(N[:mid], idx+1)
    maketree(N[mid+1:], idx+1)
maketree(node, 0)
for i in tree:
    print(*i)