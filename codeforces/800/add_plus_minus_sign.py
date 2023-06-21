for _ in range(int(input())):
    n=int(input())
    s=list(input())
    m=int(s[0])
    ans=''

    for i in range(1, n):
        m+=int(s[i])
        if m%2==1:
            ans+='+'
        else:
            ans+='-'

    print(ans)
