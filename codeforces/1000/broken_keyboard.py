for _ in range(int(input())):
    s=input()
    z=set()
    c=0
    ch=s[0]

    for i in range(len(s)):
        if s[i]==ch:
            c+=1
        else:
            if c%2==1:
                z.add(ch)
            ch=s[i]
            c=1

    if c%2==1:
        z.add(ch)
    print(''.join(sorted(list(z))))