n, m_1 = map(int, input().split())
import sys
l_1 = []
l_2 = []
for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    l_1.append(x)
m, k = map(int, input().split())
for i in range(m):
    y = list(map(int, sys.stdin.readline().split()))
    l_2.append(y)
l_ans = [[0 for _ in range(k)] for _ in range(n)]
ans = []
for i in range(n):
    for j in range(k):
        for z in range(m):
            l_ans[i][j] += l_1[i][z]*l_2[z][j]
for i in l_ans:
    print(*i)
