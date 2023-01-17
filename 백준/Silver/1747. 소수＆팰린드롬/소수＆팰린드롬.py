n = int(input())
import math
if n <= 2:
    print(2)
elif n < 4:
    print(3)
elif n < 6:
    print(5)
elif n < 8:
    print(7)
elif n >= 8 and n <= 11:
    print(11)
elif n > 11 and n <= 101:
    print(101)
else:
    def isprime(x, k):
        eratos = [1]*x
        s = int(math.sqrt(x))
        for i in range(2, s+1):
            if eratos[i] == 1:
                for j in range(i+i, x, i):
                    eratos[j] = 0
        z = k
        return [str(y) for y in range(z,x) if eratos[y] == 1 and ((str(y)[0] == "1" and str(y)[-1] == "1") or (str(y)[0] == "3" and str(y)[-1] == "3") or (str(y)[0] == "7" and str(y)[-1] == "7") or (str(y)[0] == "9" and str(y)[-1] == "9"))]
    isprime_l = isprime(1003001, n)
    c = isprime_l[0]
    k = len(isprime_l[0])
    ans = 0
    for i in range(len(isprime_l)):
        num = isprime_l[i]
        if len(num) == 3:
            ans = int(num)
            break
        elif len(num) == 4:
            if num[1] == num[2]:
                ans = int(num)
                break
        elif len(num) == 5:
            if num[1] == num[3]:
                ans = int(num)
                break
        else:
            break
    if ans == 0:
        print(1003001)
    else:
        print(ans)