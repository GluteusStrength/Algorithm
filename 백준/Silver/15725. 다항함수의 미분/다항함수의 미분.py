function = input()
function = list(function)
if ("-" not in function[1:]) and ("+" not in function):
    if "x" not in function:
        print(0)
    else:
        ans = "".join(function[:len(function)-1])
        if ans == "-":
            print(-1)
        elif ans == "":
            print(1)
        else:
            print(int(ans))
else:
    if "-" in function[1:]:
        if function[0] != "-":
            ind_minus = function.index("-")
            ans = "".join(function[:ind_minus-1])
            if ans == "":
                print(1)
            else:
                print(int(ans))
        else:
            ind_minus = function[1:].index("-") + 1
            ans = "".join(function[:ind_minus-1])
            if ans == "-":
                print(-1)
            else:
                print(int(ans))
    if "+" in function:
        ind_plus = function.index("+")
        ans = "".join(function[:ind_plus-1])
        if ans == "":
            print(1)
        elif ans == "-":
            print(-1)
        else:
            print(int(ans))