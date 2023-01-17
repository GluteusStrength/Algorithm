N = int(input())
n = str(N)
def cycle(num, cnt):
    first = int(num[0])
    second = (int(num[-1]))
    p = str(first + second)
    new = str(second) + p[-1]
    if new == n:
        cnt += 1
        return cnt
    else:
        cnt += 1
        return cycle(new, cnt)
if N < 10:
    n = "0"+n
    print(cycle(n,0))
else:
    print(cycle(n,0))

