import sys
n, p, q = map(int, sys.stdin.readline().split())
ans = {0:1, 1:2}
def inf(num):
    if num <= 1:
        return ans[num]
    else:
        if num in ans:
            return ans[num]
        ans[num] = inf(num//p) + inf(num // q)
        return ans[num]
print(inf(n))