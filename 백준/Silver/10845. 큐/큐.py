import sys
n = int(input())
q = []
for i in range(n):
    x = list(map(str, sys.stdin.readline().split()))
    if len(x) == 2:
        q.append(int(x[1]))
    else:
        if x[0] == "front":
            if q:
                print(q[0])
            else:
                print(-1)
        elif x[0] == "back":
            if q:
                print(q[-1])
            else:
                print(-1)
        elif x[0] == "empty":
            if q:
                print(0)
            else:
                print(1)
        elif x[0] == "size":
            print(len(q))
        else:
            if q:
                q = list(reversed(q))
                print(q.pop())
                q = list(reversed(q))
            else:
                print(-1)