n, k = input().split()
n = int(n)
k = int(k)
def eratos(a, b):
    a += 1
    isprime = [1] * a
    cnt = 0
    for i in range(2, a):
        if isprime[i] == 1:
            cnt += 1
            isprime[i] = 0
            if cnt == b:
                return i
            else:
                for j in range(i+i, a, i):
                    if isprime[j] == 1:
                        isprime[j] = 0
                        cnt += 1
                    else:
                        continue
                    if cnt == b:
                        return j
                    else:
                        continue
print(eratos(n, k))
