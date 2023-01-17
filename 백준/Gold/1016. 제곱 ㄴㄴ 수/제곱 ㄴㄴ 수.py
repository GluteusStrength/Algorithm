import math
import sys
mini, maxi = map(int,sys.stdin.readline().split())
def prime_list(n):
    rep = int(math.sqrt(n))+1
    if rep > 2:
        eratos = [1]*(rep+1)
        for i in range(2, rep):
            if eratos[i] == 1:
                for j in range(i+i, rep+1, i):
                    eratos[j] = 0
        return [x*x for x in range(2, len(eratos)) if eratos[x] == 1]
    else:
        return [4]
prime_l = prime_list(maxi)
number_l = [1] * (maxi-mini+1)
for i in prime_l:
    if mini % i == 0:
        s = mini // i
    else:
        s = (mini // i) + 1
    if maxi % i == 0:
        e = maxi // i
    else:
        e = int(maxi // i)
    for j in range(s, e+1):
        rem_ind = j * i - mini
        number_l[rem_ind] = 0
print(number_l.count(1))