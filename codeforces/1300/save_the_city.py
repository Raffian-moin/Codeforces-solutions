for _ in range(int(input())):
    a,b=list(map(int, input().split()))
    s='0'+input()
    z=0
    m=0
    x=0
    for i in range(len(s)-1):
        if s[i]+s[i+1]=='01':
            m+=1
            if m>1 and z*b<a:
                m-=1
                x+=z
            z=0
        elif s[i]+s[i+1]=='10':
            z=1
        elif s[i]+s[i+1]=='00':
            z+=1

    print(x*b+m*a)