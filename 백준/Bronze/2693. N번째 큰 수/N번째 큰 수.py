import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    l.sort()
    print(l[-3])