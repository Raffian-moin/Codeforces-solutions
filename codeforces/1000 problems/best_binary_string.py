for _ in range(int(input())):
    s=['0']+list(input())

    for i in range(1, len(s)):
        if s[i]=='?':
            s[i]=s[i-1]

    print(''.join(map(str, s[1:])))
