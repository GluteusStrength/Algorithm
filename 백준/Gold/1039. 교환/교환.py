from itertools import combinations
from collections import deque
from copy import deepcopy
N, k = map(int, input().split())
n = list(str(N))
if len(n) == 1:
    print(-1)
else:
    def bfs():
        MAX = 0
        visited = []
        for _ in range(len(q)): # 전의 것을 싹 다 처리해줘야한다. 앞에서 틀린 이유가 그러질 않아서다.
            check = list(q.popleft())
            comb = deque((combinations(num, 2)))
            while comb:
                cp = deepcopy(check)
                x, y = comb.popleft()
                temp = cp[y]
                cp[y] = cp[x]
                cp[x] = temp
                swap = "".join(cp)
                if swap not in visited:
                    visited.append(swap)
                    MAX = max(MAX, int(swap))
                    q.append(swap)
        return list(str(MAX))
    flag = True
    q = deque()
    q.append(n)
    flag = True
    while k > 0:
        num = [i for i in range(len(n))]
        res = bfs()
        k -= 1
        if len(res) != len(n):
            flag = False
            break
    if not flag:
        print(-1)
    else:
        print("".join(res))
