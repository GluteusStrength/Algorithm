import sys
n = int(input())
l = list(map(int, sys.stdin.readline().split()))
B,C = input().split()
b = int(B)
c = int(C)
cnt = len(l)
for i in range(len(l)):
    s = l[i]
    s -= b
    if s > 0:
        if s > c:
            if s % c != 0:
                cnt += (s//c)
                cnt += 1
            else:
                cnt += s//c
        else:
            cnt += 1
    else:
        cnt = cnt
print(cnt)
