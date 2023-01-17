n = int(input())
def isprime(i):
    import math
    i += 1
    eratos_l = [1] * i
    for x in range(2, int(math.sqrt(i))+1):
        if eratos_l[x] == 1:
            for y in range(x+x, i, x):
                eratos_l[y] = 0
    return [i for i in range(2, i) if eratos_l[i] == 1]
isprime_l = isprime(n)
cnt = 0
s = 0
e = 1
while e <= n:
    temp = sum(isprime_l[s:e])
    if temp == n:
        cnt += 1
        s += 1
    elif temp < n:
        e += 1
    else:
        s += 1
print(cnt)
