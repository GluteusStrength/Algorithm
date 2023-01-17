a, b = map(int, input().split())
arr = [0]
for i in range(1, 46):
    add = [i]*i
    arr += add
print(sum(arr[a : b+1]))