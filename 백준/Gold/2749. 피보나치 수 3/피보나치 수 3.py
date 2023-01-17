n = int(input())
fib = [0] * (1500001)
fib[1] = 1
for i in range(2, 1500001):
    fib[i] = ((fib[i-1] % 1000000) + (fib[i-2] % 1000000))%1000000
if n % 1500000 == 0:
    print(fib[-1])
else:
    print(fib[n%1500000])

