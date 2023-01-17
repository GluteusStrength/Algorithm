s = input()
t = input()
rev = list(t)
while True:
    if rev[-1] == "A":
        rev = rev[:-1]
    else:
        rev = rev[:-1]
        rev = "".join(rev)
        rev = rev[::-1]
        rev = list(rev)
    if len(rev) == len(s):
        if "".join(rev) == s:
            print(1)
            break
        else:
            print(0)
            break