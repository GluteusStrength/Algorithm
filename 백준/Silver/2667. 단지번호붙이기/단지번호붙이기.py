from collections import deque
n = int(input())
m = [list(input()) for _ in range(n)]
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]
def bfs(m, a, b):
    cnt = 1
    q = deque() # BFS를 통한 해결
    q.append((a,b))
    while q:
        f_1, f_2 = q.popleft()
        for x in range(4):
            m_1 = f_1 + mx[x]
            m_2 = f_2 + my[x]
            if (m_1 >= 0 and m_1 < n) and (m_2 >= 0 and m_2 < n):
                if m[m_1][m_2] == "1":
                    m[m_1][m_2] = "0" # 방문했으면 그냥 0으로 처리
                    q.append((m_1, m_2))
                    cnt += 1
    return cnt
res = []
for i in range(n):
    for j in range(n):
        if m[i][j] == '1':
            res.append(bfs(m, i, j))
print(len(res))
res.sort()
for i in res:
    if i == 1:
        print(i)
    else:
        print(i-1)