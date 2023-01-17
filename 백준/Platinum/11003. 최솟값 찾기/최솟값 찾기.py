import sys
from collections import deque
n, l = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))
dq = deque()
for i in range(n):
    while dq and dq[-1][1] > d[i]:
        dq.pop() # 수가 계속 증가하는 경우는 상관 없음 또 감소하는 것도 마찬가지 바로바로 출력하기 때문이다
    dq.append((i, d[i]))
    while dq and dq[0][0] < (i - l + 1):
        dq.popleft()
    print(dq[0][1], end = " ")