import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(visited):
    q = deque()
    flag = False
    for i in range(1, n-1):
        for j in range(1, m-1):
            if matrix[i][j] != 0:
                q.append((i, j))
                visited[i][j] = 1
                break
        if q:
            break
    while q:
        x, y = q.popleft()
        for mx in dx:
            for my in dy:
                if matrix[x+mx][y] != 0 and not visited[x+mx][y]:
                    q.append((x+mx, y+my))
                    visited[x+mx][y] = 1
                if matrix[x][y+my] != 0 and not visited[x][y+my]:
                    q.append((x,y+my))
                    visited[x][y+my] = 1
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j]:
                if matrix[i][j] != 0:
                    flag = True
                    break
        if flag:
            break
    return flag
t = 0
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    changed = [[0 for _ in range(m)] for _ in range(n)]
    x = bfs(visited)
    if x:
        print(t)
        break
    for i in range(1, n-1):
        for j in range(1, m-1):
            cnt = 0
            if matrix[i][j] != 0:
                changed[i][j] = matrix[i][j]
                if matrix[i-1][j] == 0:
                    cnt += 1
                if matrix[i+1][j] == 0:
                    cnt += 1
                if matrix[i][j-1] == 0:
                    cnt += 1
                if matrix[i][j+1] == 0:
                    cnt += 1
                changed[i][j] -= cnt
                if changed[i][j] < 0:
                    changed[i][j] = 0
    x = bfs(visited)
    matrix = changed
    t += 1
    # 아예 분리 안 되는 경우
    check = 0
    for i in range(n):
        check += sum(matrix[i])
    if check == 0:
        print(0)
        break