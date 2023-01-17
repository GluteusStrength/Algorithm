import sys
n = int(input())
word = [sys.stdin.readline().rstrip() for _ in range(n)]
word = list(set(word))
word.sort()
word.sort(key = len)
for i in word:
    print(i)