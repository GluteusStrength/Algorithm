import math
n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
num_list.sort()
erad = []
for j in range(1, n):
    num = num_list[j] - num_list[j-1]
    erad.append(num)
erad.sort()
s = erad[0]
for i in range(1, len(erad)):
    s = math.gcd(s, erad[i])
a = int(math.sqrt(s))
div_l = []
for i in range(2, a+1):
    if s % i == 0:
        div_l.append(i)
        div_l.append(s//i)
div_l.append(s)
div_l = list(set(div_l))
div_l.sort()
print(*div_l)

