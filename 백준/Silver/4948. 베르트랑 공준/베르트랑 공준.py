import sys
import math
def isprime(x):
    eratos = [1] * x
    for a in range(2, int(math.sqrt(x))+1):
        if eratos[a] == 1:
            for b in range(a+a, x, a):
                eratos[b] = 0
    return eratos
l = isprime(246913)
l[1] = 0
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    a = n
    b = 2 * n
    print(l[a+1:b+1].count(1))