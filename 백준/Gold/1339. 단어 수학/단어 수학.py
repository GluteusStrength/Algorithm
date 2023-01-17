import sys
n = int(input())
l = []
for i in range(n):
    l.append(sys.stdin.readline().rstrip())
num_dict = dict()
max_len = 0
for i in range(n):
    x = len(l[i])
    max_len = max(max_len, x)
word_by_ind = [[] for _ in range(max_len)]
cnt = 0
a = max_len
while cnt <= max_len:
    if cnt < max_len:
        for i in range(len(l)):
            if len(l[i]) == a:
                word_by_ind[cnt].append(l[i][0])
                l[i] = l[i][1:]
        cnt += 1
        a -= 1
    if cnt == max_len:
        break
for i in word_by_ind:
    for j in range(len(i)):
        num_dict[i[j]] = 0
for i in range(max_len):
    for j in range(len(word_by_ind[i])):
        word = word_by_ind[i][j]
        num_dict[word] += 10 ** (max_len-i-1)
num_dict = dict(sorted(num_dict.items(), key = lambda x : x[1], reverse = True))
result = 0
keys = list(num_dict.keys())
num = [0,1,2,3,4,5,6,7,8,9]
for i in keys:
    result += num_dict[i] * num[-1]
    num.remove(num[-1])
print(result)

