import sys
n = int(sys.stdin.readline())
def eratos(k):
    eratos = [1 for _ in range(k+1)]
    for i in range(2, k+1):
        if eratos[i] == 1:
            for j in range(i+i, k+1, i):
                eratos[j] = 0
    return [x for x in range(2, k+1) if eratos[x] == 1]
isprime = eratos(103)
mul_year = []
for i in range(len(isprime) - 1):
    mul_year.append(isprime[i]*isprime[i+1])
idx = 0
res = 0
for i in mul_year:
    if n > mul_year[idx]:
        idx += 1
    else:
        if n == mul_year[idx]:
            res = mul_year[idx+1]
            break
        else:
            res = mul_year[idx]
            break
print(res)