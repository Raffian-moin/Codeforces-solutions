for _ in range(int(input())):
    s = input()

    if s[0] != ")" and s[-1] != "(" and len(s) % 2 == 0:
        print("YES")
    else:
        print("NO")