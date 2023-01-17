N = input()
n = int(N)
a = n % 5
b = n // 5
if a == 0:
    print(b)
else:
    while b >= 0:
        r = n - (5 * b)
        if r % 3 == 0 and b != 0:
            s = r // 3
            print(s+b)
            break
        elif b == 0 and r % 3 != 0:
            print(-1)
            break
        elif b == 0 and r % 3 == 0:
            print(n // 3)
            break
        else:
            b -= 1