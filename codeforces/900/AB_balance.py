for _ in range(int(input())):
    s=input()
    s=[str(x) for x in s]
    s1=''

    for i in range(len(s)):
        s1+=s[i]
        if s1[0]==s1[-1]:
            s1=s[i]
    print(''.join(map(str, s[:len(s)-len(s1)]))+s1[:len(s1)-1]+s1[0])