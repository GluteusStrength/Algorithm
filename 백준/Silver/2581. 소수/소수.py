M = int(input())
N = int(input())
def isprime_sum(f):
    if f == 1:
        return False
    elif f % 2 == 0 and f != 2:
        return False
    elif f == 2 or f == 3 or f == 5 or f == 7:
        return True
    else:
        for i in range(3, int(f**0.5+1)):
            if f % i == 0:
                return False
            else:
                if f % i != 0 and i != int(f**0.5):
                    continue
                else:
                    return True
sum = 0
isprime_list = []
for i in range(M, N+1):
    f = i
    if (isprime_sum(f) == True) and i != N:
        sum += f
        isprime_list.append(f)
    elif (isprime_sum(f) == True) and i == N:
        sum += f
        isprime_list.append(f)
        print(sum)
        print(isprime_list[0])
    elif i == N and isprime_list != []:
        print(sum)
        print(isprime_list[0])
    elif i == N and isprime_list == []:
        print(-1)
    else:
        continue

