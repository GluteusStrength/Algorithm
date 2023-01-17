n = int(input())
fib = [0,1]
for i in range(1, n):
    fib.append(fib[i-1]+fib[i])
if n > 0:
    print(fib[-1])
else:
    print(0)