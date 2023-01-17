from collections import deque
import sys
A, B, C = map(int, sys.stdin.readline().split())
q = deque()
res = []
q.append((0, 0, C))
visited = [[[0 for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)]
while q:
    x = q.popleft()
    visited[x[0]][x[1]][x[2]] = 1
    if x[0] == 0:
        res.append(x[2])
    for i in range(3):
        if x[i] == 0:
            continue
        else:
            for j in range(2):
                if i == 0:
                    if j == 0:
                        if x[1] + x[0] <= B:
                            f = (0, x[0] + x[1], x[2])
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                        else:
                            f = (x[0] - (B - x[1]), B, x[2])
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                    else:
                        if x[2] + x[0] <= C:
                            f = (0, x[1], x[2] + x[0])
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                        else:
                            f = (x[0] - (C - x[2]), x[1], C)
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                elif i == 1:
                    if j == 0:
                        if x[1] + x[0] <= A:
                            f = (x[0] + x[1], 0, x[2])
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                        else:
                            f = (A, x[1] - (A - x[0]), x[2])
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                    else:
                        if x[2] + x[1] <= C:
                            f = (x[0], 0, x[2] + x[1])
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                        else:
                            f = (x[0], x[1] - (C - x[2]), C)
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                else:
                    if j == 0:
                        if x[2] + x[0] <= A:
                            f = (x[2] + x[0], x[1], 0)
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                        else:
                            f = (A, x[1], x[2] - (A - x[0]))
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                    else:
                        if x[2] + x[1] <= B:
                            f = (x[0], x[1] + x[2], 0)
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
                        else:
                            f = (x[0], B, x[2] - (B - x[1]))
                            if not visited[f[0]][f[1]][f[2]]:
                                visited[f[0]][f[1]][f[2]] = 1
                                q.append(f)
res.sort()
print(*res)