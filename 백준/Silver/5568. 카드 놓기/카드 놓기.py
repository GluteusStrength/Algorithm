from itertools import permutations
n = int(input())
k = int(input())
idx = [i for i in range(n)]
comb = list(permutations(idx, k))
nums = [input() for _ in range(n)]
res = []
for i in comb:
    ans = []
    for j in i:
        ans.append(nums[j])
    res.append("".join(ans))
print(len(list(set(res))))

