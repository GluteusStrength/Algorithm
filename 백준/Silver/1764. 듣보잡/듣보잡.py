import sys
n, m = map(int, sys.stdin.readline().split())
# set의 교집합 이용
a = set()
b = set()
for _ in range(n):
    a.add(sys.stdin.readline().rstrip())
for _ in range(m):
    b.add(sys.stdin.readline().rstrip())
x = a & b
x = list(x)
x.sort()
print(len(x))
for i in x:
    print(i)