import sys
n, k = map(int, sys.stdin.readline().split())
p = list((range(1, n+1)))
stack = []
while len(p) >= k:
    j = p[:k]
    p = p[k:]
    stack.append(str(j.pop()))
    p += j
cnt = 0
while len(p) > 1:
    if cnt == 0:
        stack.append(str(p[0]))
        p.remove(p[0])
        cnt += 1
    else:
        x = k % len(p)
        if x == 0:
            stack.append(str(p[-1]))
            p.remove(p[-1])
        else:
            z = p[:x]
            y = p[x:]
            stack.append(str(z.pop()))
            p = y+z
if p:
    stack.append(str(p[0]))
print("<", ", ".join(stack)[:], ">", sep='')