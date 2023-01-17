import sys
import re
n = int(input())
for i in range(n):
    s = sys.stdin.readline().rstrip()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(s)
    if m:
        print("YES")
    else:
        print("NO")