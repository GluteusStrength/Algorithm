from itertools import combinations_with_replacement # 중복조합
n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
c = combinations_with_replacement(nums, m)
for i in c:
    print(*i)