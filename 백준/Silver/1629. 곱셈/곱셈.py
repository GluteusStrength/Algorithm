import sys
l = list(map(int, sys.stdin.readline().split()))
a = l[0]
b = l[1]
c = l[2]
def division(a,b,c):
    if b == 1:
        return a % c
    else:
        an = division(a, b//2, c)
        if b % 2 == 0:
            return (an * an) % c
        else:
            return ((an * an) * a) % c
print(division(a,b,c))
