import sys
from collections import deque
n = int(input())
for _ in range(n):
    for i in range(2):
        if i == 0:
            n, m = map(int, sys.stdin.readline().split())
        else:
            doc = list(map(int, sys.stdin.readline().split()))
    l = deque()
    for i in range(len(doc)):
        l.append((i, doc[i]))
    cnt = 0
    while l:
        x = l.popleft()
        flag = True
        if not l:
            cnt += 1
            print(cnt)
            break
        else:
            for j in l:
                if j[1] > x[1]:
                    l.append(x)
                    flag = False
                    break
            if flag:
                cnt += 1
                if x[0] == m:
                    print(cnt)
                    break