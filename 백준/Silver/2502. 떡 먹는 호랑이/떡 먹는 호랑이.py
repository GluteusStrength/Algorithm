d, k = map(int, input().split())
fib_A = [0, 1, 0]
fib_B = [0, 0, 1]
for i in range(3, d+1):
    fib_A.append(fib_A[i-2] + fib_A[i-1])
    fib_B.append(fib_B[i-2] + fib_B[i-1])
for i in range(1, (k // fib_A[-1]) + 1):
    if (k - (fib_A[-1] * i)) % fib_B[-1] == 0:
        print(i)
        print((k - (fib_A[-1] * i)) // fib_B[-1])
        break
