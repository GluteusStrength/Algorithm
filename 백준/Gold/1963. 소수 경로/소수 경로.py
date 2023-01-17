import sys
from collections import deque

def eratos(n):
    isprime = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if not isprime[i]:
            for j in range(i+i, n+1, i):
                isprime[j] = 1
    return [str(x) for x in range(1000, n+1) if isprime[x] == 0]

prime_num = eratos(10000)

def bfs(a, b, prime_num, cnt):
    q = deque()
    q.append((a, cnt))
    visited = [0 for _ in range(10001)]
    visited[int(a)] = 1 # 방문 기록을 남겨줌
    while q:
        x, y = q.popleft()
        if x == b:
            return y
        else:
            for i in range(4):
                for j in range(10):
                    if i == 0:
                        if j > 0 and j != int(x[i]):
                            new = str(j) + x[1:]
                            if new in prime_num and not visited[int(new)]:
                                visited[int(new)] = 1
                                q.append((new, y+1))
                    else:
                        if j != int(x[i]):
                            new = x[:i]+str(j)+x[i+1:]
                            if new in prime_num and not visited[int(new)]:
                                visited[int(new)] = 1
                                q.append((new, y+1))
    return "Impossible"

t = int(input())
for i in range(t):
    a, b = map(str, sys.stdin.readline().split())
    print(bfs(a,b, prime_num, 0))