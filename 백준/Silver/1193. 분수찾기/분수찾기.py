n = int(input())
# pattern
# 1. 홀수 번째 그룹
# 분모: 오름차순, 분자: 내림차순
# 2. 짝수 번째 그룹
# 분모: 내림차순, 분자: 오름차순
a, num = 1, 2
group = 1
while n > a:
    a += num
    num += 1
    group += 1
idx = n - a + group
if group % 2 == 0:
    up = idx
    down = group - idx + 1
    print("{}/{}".format(up, down))
else:
    up = group - idx + 1
    down = idx
    print("{}/{}".format(up, down))