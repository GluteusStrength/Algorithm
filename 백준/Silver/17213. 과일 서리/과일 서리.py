n = int(input())
m = int(input())
if m < n:
    print(-1)
else:
    a = m - n
    x = a + n - 1
    y = a
    import math
    up = math.factorial(x)
    down = math.factorial(y) * math.factorial(x-y)
    print(int(up/down))