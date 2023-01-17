M = int(input())
N = int(input())
def complete(f):
    if (f ** 0.5) == int(f**0.5) :
        return True
    else:
        return False
complete_list = []
sum = 0
for i in range(M, N+1):
    f = i
    if complete(f) == True and i != N:
        sum += f
        complete_list.append(f)
    elif complete(f) == True and i == N:
        sum += f
        complete_list.append(f)
        print(sum)
        print(complete_list[0])
    elif i == N and complete_list != []:
        print(sum)
        print(complete_list[0])
    elif i == N and complete_list == []:
        print(-1)
    else:
        continue