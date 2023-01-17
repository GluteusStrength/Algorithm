import sys
N = int(input())
K = int(input())
l = sorted(list(map(int, sys.stdin.readline().split())))

if K >= N:
    print(0)
else:
    d = []
    for k in range(N-1):
        d.append(l[k+1]-l[k])
    d.sort(reverse = True)
    for x in range(K - 1):
        d.remove(d[0])
    print(sum(d))


