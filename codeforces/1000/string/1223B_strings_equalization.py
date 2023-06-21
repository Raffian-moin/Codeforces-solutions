for _ in range(int(input())):
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] in t:
            print('YES')
            break
    else:
        print('NO')