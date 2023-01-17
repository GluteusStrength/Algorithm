import sys
n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
left, right = 0, 0
ans = 2000000001
while left < n and right < n:
    flag = arr[right] - arr[left]
    if flag == m:
        ans = flag
        break
    else:
        if flag < m:
            right += 1
        else:
            ans = min(flag, ans)
            left += 1
            right = left
print(ans)
