import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
time = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(): # 실내 공기를 찾는 과정이다.
    visited = [[0]*m for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    c = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            mx = dx[i] + x
            my = dy[i] + y
            if (0 <= mx < n) and (0 <= my < m):
                if table[mx][my] == 0 and not visited[mx][my]: # 외부는 일단 바로 처리
                    q.append((mx, my))
                    visited[mx][my] = 1
                if table[mx][my] == 1:
                    visited[mx][my] += 1
                    if visited[mx][my] >= 2: # 2개 이상의 변이 접하는 경우
                        table[mx][my] = 0
                        c += 1
    return c # 실내 공기와 접촉한 치즈를 return
time = 0
while True:
    check = bfs()
    if check == 0:
        break
    else:
        time += 1
print(time)