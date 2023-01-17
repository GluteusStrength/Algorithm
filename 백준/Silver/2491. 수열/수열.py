import sys
N = input()
n = int(N)
data = list(map(int, sys.stdin.readline().split()))
cnt_list_1 = []
cnt_list_2 = []
if n == 1:
    print(1)
else:
    cnt_1 = 1
    for i in range(n-1):
        if i < n-2:
            if data[i] <= data[i+1]:
                cnt_1 += 1
            else:
                cnt_list_1.append(cnt_1)
                cnt_1 = 1
        else:
            if data[i] <= data[i+1]:
                cnt_1 += 1
                cnt_list_1.append(cnt_1)
            else:
                cnt_list_1.append(cnt_1)
                cnt_1 = 1
    cnt_2 = 1
    for j in range(n-1):
        if j < n-2 :
            if data[j] >= data[j+1]:
                cnt_2 += 1
            else:
                cnt_list_2.append(cnt_2)
                cnt_2 = 1
        else:
            if data[j] >= data[j+1]:
                cnt_2 += 1
                cnt_list_2.append(cnt_2)
            else:
                cnt_list_2.append(cnt_2)
                cnt_2 = 1
    max_1 = max(cnt_list_1)
    max_2 = max(cnt_list_2)
    print(max(2, max_1, max_2))
