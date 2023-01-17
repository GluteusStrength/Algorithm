import sys
import math
a,b = map(int, sys.stdin.readline().split())
num = b // a
if b % a != 0 or b == a:
    print(a, b)
else:
    flag = math.sqrt(num)
    l = []
    if int(flag) == flag:
        print(a,b)
    else:
        for i in range(1, int(flag) + 1):
            if num % i == 0:
                l.append(i)
    for x in range(len(l) - 1, -1, -1):
        f_2 = num // l[x]
        if math.gcd(f_2, l[x]) == 1:
            f_1 = l[x]
            break
    print(f_1 * a, f_2 * a)
