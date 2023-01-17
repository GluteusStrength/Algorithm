a,b = input().split()
a = int(a)
b = int(b)
c = a-b
if c == 0:
    print(0)
else:
    def f(x,y):
        cnt = 0
        while x >= 1:
            cnt += (x//y)
            x //= y
        return cnt
    case_1 = f(a,2) - f(b,2) - f(c,2)
    case_2 = f(a,5) - f(b,5) - f(c,5)
    print(min(case_1, case_2))