import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
for _ in range(n):
    o = sys.stdin.readline().split()
    if len(o) == 2:
        queue.append(int(o[1]))
    else:
        if o[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif o[0] == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)
        elif o[0] == "size":
            print(len(queue))
        elif o[0] == "empty":
            if queue:
                print(0)
            else:
                print(1)
        else:
            if queue:
                print(queue.popleft())
            else:
                print(-1)