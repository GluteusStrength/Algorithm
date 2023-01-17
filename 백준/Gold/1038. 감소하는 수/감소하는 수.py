import sys 
from itertools import combinations
n = int(sys.stdin.readline())
num = ["0","1","2","3","4","5","6","7","8","9"]
num_l = []
for i in range(2, 11):
    x = combinations(num, i)
    for j in x:
        y = "".join(j)
        num_l.append(int(y[::-1]))
num_l.sort()
poss = len(num_l) + 9
if n > poss:
    print(-1)
else:
    if n < 10:
        print(int(num[n]))
    else:
        print(num_l[n-10])
