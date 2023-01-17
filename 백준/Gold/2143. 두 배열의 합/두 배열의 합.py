import sys
from collections import defaultdict
t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a_res = defaultdict(int) # 지정하지 않은 키가 default로 int 0로 저장됨.
b_res = defaultdict(int)
# a_res와 b_res에 부 배열의 합 저장.
for i in range(n):
    for j in range(i+1, n+1):
        a_res[sum(a[i:j])] += 1 # 따라서 += 1 연산 가능

for i in range(m):
    for j in range(i+1, m+1):
        b_res[sum(b[i:j])] += 1

a_keys = sorted(list(a_res.keys()))
res = 0

for key in a_keys:
    if b_res[t - key] != 0:
        res += a_res[key] * b_res[t - key]
print(res)
