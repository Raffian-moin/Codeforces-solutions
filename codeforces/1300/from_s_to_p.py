for _ in range(int(input())):
    s=input()+'1'
    t=input()
    p=input()
    i=0
    while i<len(t):
        if t[i]!=s[i]:
            if t[i] not in p:
                break
            s=s[:i]+t[i]+s[i:]
            p=p.replace(t[i], "", 1)

        i+=1

    print('YES' if s[:-1]==t else 'NO')