for _ in range(int(input())):
    s=input()
    m=0

    if s[0]=='_':
        m+=1
    if s[-1]=='_':
        m+=1
    for i in range(1, len(s)):
        if s[i]=='_' and s[i-1]!='^':
            m+=1

    if s=='^':
        print(1)
    else:
        print(m)