import sys
def isprime(i):
    import math
    eratos = [1] * i
    for x in range(2, int(math.sqrt(i)+1)):
        if eratos[x] == 1:
            for y in range(x+x, i, x):
                eratos[y] = 0
    return eratos
l = isprime(1000001)
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for a in range(3, n//2 + 1, 2):
        k = n - a
        cnt = 0
        if l[a] == 1 and l[n-a] == 1:
            print("{} = {} + {}".format(n,a,k))
            break

