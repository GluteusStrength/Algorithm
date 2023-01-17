n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
def isprime(i):
    import math
    f = i
    for x in range(2, int(math.sqrt(f))+1):
        if f % x == 0:
            return False
        else:
            if f % x != 0 and x == int(math.sqrt(f)):
                return True
            else:
                continue

isprime_l = [2,3]
k = max(l)
for i in range(2, k):
    if isprime(i) == True:
        isprime_l.append(i)
for j in range(n):
    a = l[j]
    isprime_p = []
    if a == k:
        isprime_p = isprime_l
    else:
        for k in range(len(isprime_l)):
            if isprime_l[k] < a:
                isprime_p.append(isprime_l[k])
            else:
                break
    diff_l = []
    for x in range(len(isprime_p)):
        for y in range(x+1):
            if isprime_l[x] + isprime_l[y] == a:
                diff_l.append((isprime_l[x],isprime_l[y]))
            if isprime_l[x] + isprime_l[y] > a:
                break
    min_diff_l = diff_l[0]
    print(min_diff_l[1], min_diff_l[0])
