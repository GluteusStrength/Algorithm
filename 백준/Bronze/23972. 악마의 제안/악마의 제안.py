import sys
k, n = map(int, sys.stdin.readline().split())
if n == 1:
    print(-1)
else:
    flag = (n * k) / (n - 1)
    if flag < 0:
        print(-1)
    else:
        if n > k:
            print(k+1)
        else:
            if flag == int(flag):
                if (int(flag) - k) * n >= int(flag):
                    print(int(flag))
                else:
                    print(int(flag)+1)
            else:
                print(int(flag) + 1)
