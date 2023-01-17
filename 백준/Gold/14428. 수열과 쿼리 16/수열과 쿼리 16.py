import sys, math
def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        init(node * 2, start, mid) # 일단 재귀로 리프노드까지 진행
        init(node * 2 + 1, mid + 1, end) # 오른쪽 노드
        tree[node] = min(tree[node*2], tree[node*2+1]) # 부모노드는 자식노드들의 최소값으로

def query(node, start, end, left, right):
    if end < left or start > right:
        return math.inf
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return min(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))

def update(node, start, end, ind, change):
    if start > ind or end < ind:
        return math.inf
    if start == end:
        tree[node] = change
        return tree[node]
    mid = (start + end) // 2
    update(node*2, start, mid, ind, change)
    update(node*2+1, mid+1, end, ind, change)
    tree[node] = min(tree[node*2], tree[node*2+1])

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
tree = [0] * (4*n)
init(1, 0, n-1)
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    if x == 1:
        arr[y-1] = z
        update(1, 0, n-1, y-1, z)
    if x == 2:
        ans = query(1, 0, n-1, y-1, z-1)
        for i in range(y-1, z):
            if arr[i] == ans:
                print(i+1)
                break
