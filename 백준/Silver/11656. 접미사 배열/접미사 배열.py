s = input()
res = []
for i in range(len(s)):
    res.append(s[i:])
res.sort()
for i in res:
    print(i)