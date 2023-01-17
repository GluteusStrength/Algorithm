import sys
a, b = map(int, sys.stdin.readline().split())
if a == b:
    print(1)
else:
    def find(x,y,cnt):
        if (y % 10) % 2 != 0:
            if y % 10 == 1:
                if y == x:
                    return cnt
                else:
                    cnt += 1
                    y //= 10
                    return find(x, y, cnt)
            else:
                if y == x:
                    return cnt
                else:
                    return -1
        else:
            if y >= x:
                if y > x:
                    cnt += 1
                    y //= 2
                    return find(x,y,cnt)
                else:
                    return cnt
            else:
                return -1
    print(find(a,b,1))