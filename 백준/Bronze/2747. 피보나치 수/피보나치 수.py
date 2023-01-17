n = int(input())
fib = [0,1]
for i in range(1,n):
    fib.append(fib[i]+fib[i-1])
print(fib[-1])