import sys
n, k = map(int, sys.stdin.readline().split())
p = 1000000007
def power(a, b):
    if b == 0:
        return 1
    else:
        if b % 2 == 0:
            return (power(a, b//2) ** 2) % p
        else:
            return (power(a, b//2) ** 2 * a) % p
fact_list = [1 for i in range(n+1)]
for i in range(2, n+1):
    fact_list[i] = (fact_list[i-1] * i) % p
A = fact_list[n]
B = fact_list[n-k] * fact_list[k]
print(((A%p) * (power(B, p-2))%p)%p)