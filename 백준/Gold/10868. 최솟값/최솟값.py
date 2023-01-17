import sys, math

def min_init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(min_init(node*2, start, mid), min_init(node*2+1, mid+1, end))
    return tree[node]

def query_min(node, start, end, left, right):
    if end < left or start > right:
        return math.inf
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(query_min(node*2, start, mid, left, right), query_min(node*2+1, mid+1, end, left, right))


n, m = map(int, sys.stdin.readline().split())
tree = [0] * (4*n)
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
min_init(1, 0, n-1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(query_min(1, 0, n-1, a-1, b-1))