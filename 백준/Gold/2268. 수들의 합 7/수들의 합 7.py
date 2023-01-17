import sys
def seg_init(node, start, end):
    # 재귀로 segment tree 초기 배열의 합 구현
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = seg_init(node*2, start, mid) + seg_init(node*2 + 1, mid + 1, end)
        return tree[node]
# 구간 합 구하기
# node가 담당하는 구간: [start, end]
# 합을 구해야 하는 구간: [left, right]
def subSum(node, start, end, left, right):
    if end < left or start > right: # 아예 겹치지 않는 경우
        return 0
    if left <= start and right >= end: # [start, end]를 [left, right]가 완전히 포함
        return tree[node]
    # 그렇지 않으면 두 부분으로 나누어 합을 구한다.
    mid = (start + end) // 2
    return subSum(node * 2, start, mid, left, right) + subSum(node * 2 + 1, mid + 1, end, left, right)

# 값 수정하기
# 부모 노드가 해당 것을 포함하면 모두 변경해줘야 한다.
def update(node, start, end, ind, change):
    if start > ind or end < ind:
        return
    tree[node] += change
    if start != end: # 리프 노드가 아닌 경우
        mid = (start+end) // 2
        update(node * 2, start, mid, ind, change)
        update(node * 2 + 1, mid + 1, end, ind, change)
n, m = map(int, sys.stdin.readline().split())
nums = [0] * n
tree = [0] * (4*n)
seg_init(1, 0, n-1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        b -= 1 # 원래의 트리는 index가 0부터 시작
        change = c - nums[b]
        nums[b] = c
        update(1, 0, n-1, b, change)
    if a == 0:
        if b > c:
            temp = c
            c = b
            b = temp
        print(subSum(1, 0, n-1, b-1, c-1))