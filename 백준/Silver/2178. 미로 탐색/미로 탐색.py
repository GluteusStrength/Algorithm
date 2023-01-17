from collections import deque
n, m = map(int, input().split())
maze = []
for i in range(n):
    k = input()
    maze.append(list(k))
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
q = deque()
q.append([0,0])
route = 0
while q:
    f = q.popleft()
    x, y = f
    if x == n - 1 and y == m - 1:
        break
    else:
        if x-1 >= 0 and maze[x-1][y] == "1":
            if not visited[x-1][y]:
                q.append([x-1, y])
                visited[x-1][y] = visited[x][y] + 1
        if x+1 < n and maze[x+1][y] == "1":
            if not visited[x+1][y]:
                q.append([x+1, y])
                visited[x+1][y] = visited[x][y] + 1
        if y-1 >= 0 and maze[x][y-1] == "1":
            if not visited[x][y-1]:
                q.append([x, y-1])
                visited[x][y-1] = visited[x][y] + 1
        if y+1 < m and maze[x][y+1] == "1":
            if not visited[x][y+1]:
                q.append([x, y+1])
                visited[x][y+1] = visited[x][y] + 1
print(visited[n-1][m-1])