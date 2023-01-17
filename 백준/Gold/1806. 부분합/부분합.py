import sys
n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sum_list = [0 for _ in range(n+1)]
for i in range(1, n+1):
    sum_list[i] = (nums[i-1] + sum_list[i-1]) # 누적합
start = 0
end = 1
length = n+1
while start != n:
    if sum_list[end] - sum_list[start] >= s:
        length = min(length, end - start)
        start += 1
    else:
        if end < n:
            end += 1
        else:
            start += 1
if length != n+1:
    print(length)
else:
    print(0)