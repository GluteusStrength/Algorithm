import sys # 볼록, 오목 다각형 등 여러 다각형에서 사선 공식을 쓸 수 있다.
import math
a = []
n = int(input())
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
front = 0
back = 0
a.append(a[0])
for i in range(n):
    front += a[i][0] * a[i+1][1]
    back += a[i][1] * a[i+1][0]
    ans = front - back
ans = math.fabs(ans) * 0.5
print("%.1f" % ans)


