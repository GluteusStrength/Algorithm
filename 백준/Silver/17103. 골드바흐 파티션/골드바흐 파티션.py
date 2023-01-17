t = int(input())
import sys
def eratos(k):
    k+=1
    isprime = [1] * k
    for i in range(2, k):
        if isprime[i] == 1:
            for j in range(i+i, k, i):
                isprime[j] = 0
    return isprime
l = eratos(1000000)
for i in range(t):
    n = int(sys.stdin.readline())
    if n == 4:
        print(1)
    else:
        cnt = 0
        for a in range(3, n//2 + 1, 2):
            if l[a] == 1 and l[n-a] == 1:
                cnt += 1
        print(cnt)