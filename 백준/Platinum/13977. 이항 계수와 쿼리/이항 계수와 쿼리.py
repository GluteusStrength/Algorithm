import sys
m = int(sys.stdin.readline())
p = 1000000007
fact_list = [1 for i in range(4000001)]
for i in range(2, 4000001):
    fact_list[i] = (fact_list[i - 1] * i) % p
for _ in range(m):
    n, k = map(int, sys.stdin.readline().split())
    def power(a, b):
        if b == 0:
            return 1
        else:
            if b % 2 == 0:
                return (power(a, b//2) ** 2) % p
            else:
                return (power(a, b//2) ** 2 * a) % p
    A = fact_list[n]
    B = fact_list[n-k] * fact_list[k]
    print(((A%p) * (power(B, p-2))%p)%p)