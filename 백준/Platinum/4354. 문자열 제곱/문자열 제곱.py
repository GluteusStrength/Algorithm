import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    else:
        pi = [0 for _ in range(len(s))]
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = pi[j-1]
            if s[i] == s[j]:
                j += 1
                pi[i] = j
        x = len(s) - pi[-1]
        if len(s) % x == 0:
            print(len(s)//x)
        else:
            print(1)