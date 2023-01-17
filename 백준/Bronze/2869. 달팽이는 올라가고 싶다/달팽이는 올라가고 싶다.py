import sys
l = list(map(int, sys.stdin.readline().split()))
a = l[0]
b = l[1]
v = l[2]
if a >= v:
    print(1)
elif a < v and a <= b:
    print(-1)
else:
    h = a - b
    s = (v - a) // h
    if s < 1:
        s += 1
    else:
        if (v-a) % h != 0:
            s+=1
    print(s+1)