import sys
n, x = map(int, sys.stdin.readline().split())
re = 0
flag = n
if n * 26 < x or n > x: # 무조건 안 되는 조건 생각
    print("!")
else:
    s = ["A" for _ in range(n)]
    x -= n
    while True:
        rept = x // 26
        surp = x % 26
        if rept >= 1:
            for i in range(flag-1, flag-rept-1, -1):
                s[i] = "Z"
            x %= 26
            x += rept
            flag -= rept
        else:
            change = chr(ord("A")+surp)
            s[flag-1] = change
            break
    print("".join(s))