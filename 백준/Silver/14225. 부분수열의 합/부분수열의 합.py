n = int(input())
s = list(map(int, input().split()))
s.sort()
num = 0
for i in s:
    if num + 1 < i:
        break
    num += i
print(num+1)



