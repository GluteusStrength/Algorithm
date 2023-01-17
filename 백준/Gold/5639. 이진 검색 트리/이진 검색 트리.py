import sys
# 재귀 limit
sys.setrecursionlimit(10 ** 6)

def post_order(start, end):
    if start > end:
        return
    root = pre_order[start]
    flag = start + 1
    # 왼, 오른쪽 서브트리 구분
    while flag <= end:
        if pre_order[flag] > root:
            break
        flag += 1
    # 왼쪽 서브트리 탐색
    post_order(start + 1, flag - 1)
    # 오른쪽 서브트리 탐색
    post_order(flag, end)
    # root 출력
    print(root)
    
pre_order = []
while True:
    try:
        pre_order.append(int(sys.stdin.readline()))
    except:
        break
post_order(0, len(pre_order) - 1)
