n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
left = []
right = []
ans = 0
for i in nums:
    if i <= 0:
        left.append(i)
    else:
        right.append(i)
def sum(l, x):
    if l:
        if l[-1] > 0: # right가 들어오는 case
            if 1 not in l:
                while len(l) > 1:
                    r = 1
                    for i in range(2):
                        r *= l.pop()
                    x += r
                if l:
                    x += l.pop()
                    return x
                else:
                    return x
            else:
                k = 0
                while 1 in l:
                    k += 1
                    l.remove(1)
                while len(l) > 1:
                    r = 1
                    for _ in range(2):
                        r *= l.pop()
                    x += r
                if l:
                    x += l.pop()
                    return x + k
                else:
                    return x + k
        else: # left가 들어오는 case
            while len(l) > 1:
                r = 1
                for _ in range(2):
                    r *= l[0]
                    l.remove(l[0])
                x += r
            if l:
                x += l.pop()
                return x
            else:
                return x
    else:
        return x
ans += sum(right, 0)
ans += sum(left, 0)
print(ans)
