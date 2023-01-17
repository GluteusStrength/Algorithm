N = input()
n = int(N)
w = int(input())
cnt = 1
l = []
l.append(w)
if n >= 6:
    print("Love is open door")
else:
    for i in range(n-1):
        if l[i] == 0:
            l.append(1)
        else:
            l.append(0)
    for j in range(1,n):
        print(l[j])