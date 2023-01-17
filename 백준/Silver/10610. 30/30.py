import sys
n = list(sys.stdin.readline())
n.remove("\n")
n.sort(reverse=True)
if "0" not in n:
    print(-1)
else:
    cnt = 0
    for i in n:
        cnt += int(i)
    if cnt % 3 != 0:
        print(-1)
    else:
        print(int("".join(n)))




