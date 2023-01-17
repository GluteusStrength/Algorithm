import sys
from math import factorial
n, k, m = map(int, sys.stdin.readline().split())

# 이항 계수 구하기, 뤼카의 정리
def comb(n,r):
    if n < r:
        return 0
    else:
        return factorial(n)//(factorial(n-r)*factorial(r))

ans = 1
while (n != 0 and k != 0):
    ans = ans*comb(n % m, k % m) % m
    n //= m
    k //= m

print(ans % m)

