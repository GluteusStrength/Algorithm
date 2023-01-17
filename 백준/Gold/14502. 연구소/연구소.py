import sys, copy
from collections import deque
n, m = map(int, sys.stdin.readline().split())
virus = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]
ans = 0
def bfs():
    global ans
    v = copy.deepcopy(virus) # 깊은 복사를 통해 영향을 안 미치게 한다.
    q = deque()
    for i in range(n):
        for j in range(m):
            if v[i][j] == 2:
                q.append((i,j))
    while q:
        x = q.popleft()
        a, b = x
        for i in range(4):
            if 0 <= a + mx[i] < n and 0 <= b + my[i] < m:
                if v[a+mx[i]][b+my[i]] == 0:
                    v[a+mx[i]][b+my[i]] = 2
                    q.append((a+mx[i], b+my[i]))
    cnt = 0
    for i in v:
        cnt += i.count(0)
    ans = max(ans, cnt)
    return ans

def make_wall(x):
    if x == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if virus[i][j] == 0:
                    virus[i][j] = 1
                    make_wall(x+1)
                    virus[i][j] = 0 # 다시 초기화
make_wall(0)
print(ans)