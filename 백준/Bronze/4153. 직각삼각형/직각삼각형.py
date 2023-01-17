import sys
while True:
    l = list(map(int, sys.stdin.readline().split()))
    if 0 in l:
        break
    else:
        l.sort()
        if l[2]*l[2] == l[1]*l[1] + l[0]*l[0]:
            print("right")
        else:
            print("wrong")