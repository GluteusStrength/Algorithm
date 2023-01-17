n = int(input())
dp = [0] * (n+1)
num_list = []
for i in range(1, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
length = dp[-1] - 1
number = n
while length > 0:
    if number % 3 == 0:
        if dp[number // 3] == length:
            num_list.append(number)
            number = number // 3
            length -= 1
    if number % 2 == 0:
        if dp[number // 2] == length:
            num_list.append(number)
            number = number // 2
            length -= 1
    if (number % 3 != 0 and number % 2 != 0) or dp[number // 3] != length or dp[number // 2] != length:
        if dp[number - 1] == length:
            num_list.append(number)
            number = number - 1
            length -= 1
print(dp[n] - 1)
if 1 not in num_list:
    num_list.append(1)
    print(*num_list)
else:
    print(*num_list)
