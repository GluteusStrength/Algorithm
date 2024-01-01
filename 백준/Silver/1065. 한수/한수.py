import sys
N = int(sys.stdin.readline().strip())
if N <= 99:
    print(N)
else:
    n = N // 100
    cnt = 99
    cnt += (n-1) * 5
    num_list = []
    for i in range(n*100, N+1):
        a = i // 100
        b = (i - 100 * a) // 10
        c = i - a * 100 - b * 10
        if a-b == b-c:
            num_list.append(i)
    cnt += len(num_list)
    print(cnt)