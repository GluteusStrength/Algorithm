n = int(input())
def isprime(x):
    eratos = [1 for _ in range(x+1)]
    for i in range(2, x+1):
        if eratos[i] == 1:
            for j in range(i+i, x+1, i):
                eratos[j] = 0
    return [y for y in range(2, len(eratos)) if eratos[y] == 1]
isprime_list = isprime(1299709)
for i in range(n):
    num = int(input())
    if num in isprime_list:
        print(0)
    else:
        left = 0
        right = len(isprime_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if isprime_list[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        print(isprime_list[left] - isprime_list[right])
