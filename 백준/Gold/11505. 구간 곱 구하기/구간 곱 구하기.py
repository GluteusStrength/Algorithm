import sys
mod = 1000000007
def seg_init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = (seg_init(node*2, start, mid) * seg_init(node*2 + 1, mid + 1, end)) % mod
        return tree[node]

def subMul(node, start, end, left, right):
    if end < left or start > right: # 아예 겹치지 않는 경우
        return 1
    if left <= start and right >= end: # [start, end]를 [left, right]가 완전히 포함
        return tree[node] % mod
    mid = (start + end) // 2
    return (subMul(node * 2, start, mid, left, right) * subMul(node * 2 + 1, mid + 1, end, left, right)) % mod


def update(node, start, end, ind, change):
    if start > ind or end < ind:
        return
    if start == end: # 그 부분을 바꿔준다
        tree[node] = change
    else:
        mid = (start+end) // 2
        update(node * 2, start, mid, ind, change)
        update(node * 2 + 1, mid + 1, end, ind, change)
        tree[node] = (tree[node*2] * tree[node*2 + 1]) % mod

n, m, k = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
tree = [0] * (4*n)
seg_init(1, 0, n-1)
for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        nums[b-1] = c
        update(1, 0, n-1, b-1, c)
    if a == 2:
        print(subMul(1, 0, n-1, b-1, c-1))