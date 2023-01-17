import sys
from collections import deque
n = int(sys.stdin.readline())
d_q = deque()
for _ in range(n):
    order = sys.stdin.readline().split()
    if len(order) == 2:
        if order[0] == "push_back":
            d_q.append(order[1])
        else:
            d_q.appendleft(order[1])
    else:
        if order[0] == "front":
            if d_q:
                print(d_q[0])
            else:
                print(-1)
        elif order[0] == "back":
            if d_q:
                print(d_q[-1])
            else:
                print(-1)
        elif order[0] == "empty":
            if d_q:
                print(0)
            else:
                print(1)
        elif order[0] == "size":
            print(len(d_q))
        elif order[0] == "pop_front":
            if d_q:
                print(d_q.popleft())
            else:
                print(-1)
        elif order[0] == "pop_back":
            if d_q:
                print(d_q.pop())
            else:
                print(-1)
        else:
            continue
