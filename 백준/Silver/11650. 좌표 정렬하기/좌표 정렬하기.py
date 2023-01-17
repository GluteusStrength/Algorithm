import sys
n = int(input())
d = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d.sort(key = lambda x : (x[0], x[1]))
for i in d:
    print(i[0], i[1])