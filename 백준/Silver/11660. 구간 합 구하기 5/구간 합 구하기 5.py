import sys
n, m = map(int, sys.stdin.readline().split())
matrix = [[0] for _ in range(n+1)]
matrix[0] = [0,0,0,0,0]
for i in range(1, n+1):
    matrix[i] += (list(map(int, sys.stdin.readline().split())))
s = [[0 for _ in range(n+1)] for _ in range(n+1)]
t = s
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            s[i][j] = matrix[i][j]
        elif i == 1 and j != 1:
            s[i][j] = s[i][j-1] + matrix[i][j]
        elif i != 1 and j == 1:
            s[i][j] = s[i-1][1] + matrix[i][j]
        else:
            s[i][j] = s[i-1][j] + sum(matrix[i][:j+1])
for x in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    ans = s[c][d] - s[c][b-1] - s[a-1][d] + s[a-1][b-1]
    print(ans)

