import sys
n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
d = list(map(int, sys.stdin.readline().split()))
card.sort()
def binary_search(left, right, t):
    if left > right:
        print(0, end = " ")
        return 0
    else:
        mid = (left + right) // 2
        if card[mid] == t:
            print(1, end = " ")
            return 1
        else:
            if card[mid] < t:
                binary_search(mid + 1, right, t)
            else:
                binary_search(left, mid - 1, t)
for i in d:
    binary_search(0, n-1, i)
