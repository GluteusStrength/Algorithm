N = input()
n = int(N)
if n == 1:
    print(1)
else:
    if n <= 7:
        print(2)
    else:
        k = 1
        l = []
        s = 1
        while (6 * k + 1) < n:
            s += 1
            k += s
            l.append(s)
        ans = l[-1] + 1
        print(ans)