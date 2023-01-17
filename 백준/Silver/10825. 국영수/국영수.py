import sys
n = int(input())
l = [sys.stdin.readline().split() for _ in range(n)]
for i in l:
    i[1] = int(i[1])
    i[2] = int(i[2])
    i[3] = int(i[3])
l.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in l:
    print(i[0])