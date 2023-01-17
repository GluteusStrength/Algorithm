import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
m = 100001
visited = [-1] * m
check = [0] * m
q = deque()
visited[n] = 0
q.append(n)
def path(x):
    move = []
    temp = x
    for _ in range(visited[x] + 1):
        move.append(temp)
        temp = check[temp]
    print(*move[::-1])
while q:
    x = q.popleft()
    if x == k:
        print(visited[x])
        path(x)
        break
    else:
        for i in [2*x, x-1, x+1]:
            if (0 <= i <= (m-1)) and visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)
                check[i] = x # 이동 경로 저장
