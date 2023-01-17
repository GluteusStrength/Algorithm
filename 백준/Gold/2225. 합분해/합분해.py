n, k = map(int, input().split())
a = n+1
s = [[0] * a for x in range(k)]
cnt = 0
for y in range(len(s[0])):
    s[0][y] = 1
for z in range(len(s)):
    s[z][0] = 1
for i in range(k-1):
    for j in range(1, n+1):
        s[i+1][j] = s[i][j] + s[i+1][j-1]
print(s[k-1][n] % 1000000000)

