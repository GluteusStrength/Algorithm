import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
pi = [0 for _ in range(n)]
j = 0
for i in range(1, n):
    while j > 0 and s[i] != s[j]:
        j = pi[j-1]
    if s[i] == s[j]:
        j += 1
        pi[i] = j
print(len(s) - pi[-1])