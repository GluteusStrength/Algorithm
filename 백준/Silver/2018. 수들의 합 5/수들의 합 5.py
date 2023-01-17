n = int(input())
start = 0
end = 1
flag = 0
cnt = 0
if n >= 5:
    while start <= n//2 + 1:
        if flag < n:
            flag += end
            end += 1
        elif flag == n:
            cnt += 1
            start += 1
            flag -= start
        else:
            start += 1
            flag -= start
    print(cnt+1)
else:
    x = [0, 1, 1, 2, 1]
    print(x[n])