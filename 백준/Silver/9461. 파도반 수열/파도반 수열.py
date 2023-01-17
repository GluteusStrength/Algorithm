T = input()
t = int(T)
n_list = []
for i in range(t):
    n_list.append(int(input()))
pad = [1,1,1,2,2]
for j in range(t):
    n = n_list[j]
    if n < 6:
        print(pad[n-1])
    else:
        for k in range(5, n):
            pad_n = pad[k-5] + pad[k-1]
            pad.append(pad_n)
        print(pad[n-1])
        pad = [1,1,1,2,2]