n = int(input())
fib = [0, 1]
for i in range(2, abs(n)+1):
    fib.append((fib[i-1] + fib[i-2]) % 1000000000)
if n == 0:
    print(0)
elif n < 0:
    if abs(n) % 2 != 0:
        print(1)
    else:
        print(-1)
else:
    print(1)
print(fib[abs(n)] % 1000000000)

