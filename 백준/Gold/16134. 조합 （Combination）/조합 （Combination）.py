import sys, math
n, r = map(int, sys.stdin.readline().split())
mod = 1000000007
print((math.factorial(n)//(math.factorial(n-r)*math.factorial(r)))%mod)