n = int(input())
dp = [1 for _ in range(n)]
student = []
for i in range(n):
    student.append(int(input()))
for i in range(1, n):
    for j in range(i):
        if student[i] > student[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))