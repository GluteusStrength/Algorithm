import sys
from collections import Counter
n = int(input())
s = list(map(int, sys.stdin.readline().split()))
s = Counter(s)
m = int(input())
c = list(map(int, sys.stdin.readline().split()))
ans = []
for i in c:
    if i in s:
        ans.append(s[i])
    else:
        ans.append(0)
print(*ans)
