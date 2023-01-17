import sys
s = sys.stdin.readline().rstrip()
stack = []
idx = 0
s_1 = ""
s_2 = ""
ans = ""
flag = False
while idx < len(s):
    # <를 만나는 경우? -> >를 만날 때까지 그냥 쭉 진행한다.
    if s[idx] == "<":
        if s_2:
            ans += s_2[::-1]
            s_2 = ""
        s_1 += s[idx]
        idx += 1
        flag = True
    elif s[idx] == ">":
        s_1 += s[idx]
        idx += 1
        flag = False
        ans += s_1
        s_1 = ""
    else:
        if flag == True:
            s_1 += s[idx]
            idx += 1
        else:
            if s[idx] != " ":
                s_2 += s[idx]
                idx += 1
            else:
                ans += s_2[::-1]
                ans += s[idx]
                idx += 1
                s_2 = ""
if s_2:
    ans += s_2[::-1]
    print(ans)
else:
    print(ans)





