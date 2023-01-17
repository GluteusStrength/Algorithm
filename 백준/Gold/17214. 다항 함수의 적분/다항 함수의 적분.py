d = input()
if d == "0":
    print("W")
else:
    if "+" in d:
        ind_p = d.index("+")
        l_1 = []
        l_2 = []
        for i in range(ind_p):
            l_1.append(d[i])
        for j in range(ind_p+1, len(d)):
            l_2.append(d[j])
        l_1.append("x")
        l_2.append("x")
        a = "".join(l_1[0:ind_p-1])
        new_a = str(int("".join(a)) // 2)
        l_1[0] = new_a
        f_a = l_1[0]+l_1[-1]+l_1[-2]
        f_b = "".join(l_2)
        if "1" in f_a and len(f_a) == 3 and d[0] != "-":
            f_a = f_a.replace("1", "")
            if "1" in f_b and len(f_b) == 2:
                f_b = f_b.replace("1", "")
                ans = f_a+"+"+f_b+"+"+"W"
                print(ans)
            else:
                print(f_a+"+"+f_b+"+"+"W")
        elif "1" in f_a and len(f_a) == 4 and d[0] == "-":
            f_a = f_a.replace("1", "")
            if "1" in f_b and len(f_b) == 2:
                f_b = f_b.replace("1", "")
                ans = f_a+"+"+f_b+"+"+"W"
                print(ans)
            else:
                print(f_a+"+"+f_b+"+"+"W")
        else:
            if "1" in f_b and len(f_b) == 2:
                f_b = f_b.replace("1", "")
                ans = f_a+"+"+f_b+"+"+"W"
                print(ans)
            else:
                print(f_a+"+"+f_b+"+"+"W")
    else:
        if "x" in d:
            l_3 = []
            for i in range(len(d)):
                l_3.append(d[i])
            if "-" in d[1:] and d[0] != "-":
                m_ind = d[0:].index("-")
                a = "".join(l_3[0 : m_ind-1])
                new_a = str(int("".join(a)) // 2)
                l_3[0] = new_a
                l_3[0] = l_3[0]+"x"+"x"
                b = "".join(l_3[m_ind+1:])
                b += "x"
                if "1" in l_3[0] and len(l_3[0]) == 3:
                    l_3[0] = l_3[0].replace("1", "")
                    if "1" in b and len(b) == 2:
                        b = b.replace("1", "")
                        print(l_3[0]+"-"+b+"+"+"W")
                    else:
                        print(l_3[0] + "-" + b + "+" + "W")
                else:
                    if "1" in b and len(b) == 2:
                        b = b.replace("1", "")
                        print(l_3[0]+"-"+b+"+"+"W")
                    else:
                        print(l_3[0] + "-" + b + "+" + "W")
            elif "-" in d[1:] and d[0] == "-":
                m_ind = (d[1:].index("-"))+1
                a = "".join(l_3[0:m_ind-1])
                new_a = str(int(a)//2)
                l_3[0] = new_a+"x"+"x"
                b = "".join(l_3[m_ind+1:])
                b += "x"
                if "1" in l_3[0] and len(l_3[0]) == 4:
                    l_3[0] = l_3[0].replace("1", "")
                    if "1" in b and len(b) == 2:
                        b = b.replace("1", "")
                        print(l_3[0]+"-"+b+"+"+"W")
                    else:
                        print(l_3[0]+"-"+b+"+"+"W")
                else:
                    if "1" in b and len(b) == 2:
                        b = b.replace("1", "")
                        print(l_3[0]+"-"+b+"+"+"W")
                    else:
                        print(l_3[0]+"-"+b+"+"+"W")
            else:
                x_ind = d.index("x")
                a = "".join(l_3[0 : x_ind])
                new_a = str(int("".join(a)) // 2)
                if "1" in new_a and len(new_a) == 1 and d[0] != "-":
                    new_a = new_a.replace("1", "")
                    print(new_a + "x" + "x" + "+" + "W")
                elif "1" in new_a and len(new_a) == 2 and d[0] == "-":
                    new_a = new_a.replace("1", "")
                    print(new_a + "x" + "x" + "+" + "W")
                else:
                    print(new_a + "x" + "x" + "+" + "W")
        else:
            a = int(d)
            new_a = a
            if new_a == 1 or new_a == -1:
                ans_a = str(new_a).replace("1","x")
                print(ans_a+"+"+"W")
            else:
                print(str(new_a)+"x"+"+"+"W")