import sys
n = int(sys.stdin.readline())
s = set()
for i in range(n):
    order = sys.stdin.readline().split() # 이 자체가 list
    if len(order) == 1:
        if order[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        x = int(order[1])
        if order[0] == "add":
            s.add(x)
        elif order[0] == "remove":
            s.discard(x)
        elif order[0] == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)
        else:
            if x in s:
                print(1)
            else:
                print(0)