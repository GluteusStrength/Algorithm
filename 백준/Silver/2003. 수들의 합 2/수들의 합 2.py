import sys
n, m = map(int, sys.stdin.readline().split())
s = [0] + list(map(int, sys.stdin.readline().split()))
start = 0
end = 1
cnt = 0
prefix_sum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + s[i]
while start < n:
    if end < n:
        if prefix_sum[end] - prefix_sum[start] < m:
            end += 1
        elif prefix_sum[end] - prefix_sum[start] == m:
            cnt += 1
            end += 1
        else:
            start += 1
    else:
        if prefix_sum[end] - prefix_sum[start] == m:
            cnt += 1
        start += 1
print(cnt)