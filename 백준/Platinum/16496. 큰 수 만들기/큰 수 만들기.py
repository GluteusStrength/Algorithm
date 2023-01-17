import sys
n = int(input())
nums = list(map(str, sys.stdin.readline().split()))
nums = sorted(nums, key = lambda x : x*10, reverse = True)
print(int("".join(nums)))