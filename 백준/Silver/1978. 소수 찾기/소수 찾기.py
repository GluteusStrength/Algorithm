import sys
k = int(input())
l = sorted(list(map(int, sys.stdin.readline().split())))
ans = 0
def isprime(f):
    if f == 1 :
        return False
    elif f == 2 or f == 3 or f == 5 or f == 7:
        return True
    elif f % 2 == 0 and f != 2:
        return False
    else:
        for i in range(3, int(f**0.5+1)):
            if f % i == 0:
                return False
            else:
                if f % i != 0 and i != int(f**0.5):
                    continue
                else:
                    return True
for a in range(len(l)):
    f = l[a]
    if isprime(f) == True:
        ans += 1
    else:
        continue
print(ans)