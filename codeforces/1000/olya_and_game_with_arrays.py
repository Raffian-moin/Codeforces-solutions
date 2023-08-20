for _ in range(int(input())):
    n=int(input())
    a=[]
    mi=1e9+1
    s=0
    ans=0
    for _ in range(n):
        m=int(input())
        b=list(map(int, input().split()))
        b.sort()
        a.append(b[1])
        s+=b[1]
        mi=min(b[0], mi)

    for el in a:
        ans=max(ans, s+mi-el)

    print(ans)