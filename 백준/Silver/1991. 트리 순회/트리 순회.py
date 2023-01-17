import sys
n = int(input())
tree = {}
for i in range(n):
    root, l, r = map(str, sys.stdin.readline().split())
    tree[root] = [l, r]
def preorder(root):
    if root != ".":
        print(root, end = "") # 부모노드는 바로 출력
        preorder(tree[root][0]) # 왼쪽노드를 우선 방문
        preorder(tree[root][1]) # 오른쪽노드는 후에 방문

def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end = "")
        inorder(tree[root][1])

def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = "")
# 전반적인 큰 틀은 재귀로 처리 가능

preorder("A")
print()
inorder("A")
print()
postorder("A")