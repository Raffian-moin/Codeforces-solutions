for _ in range(int(input())):
    n,k,d,w=list(map(int, input().split()))
    a=list(map(int, input().split()))
    t=a[0]+d+w
    ans=1
    c=1

    for i in range(n):
        if t<a[i] or c>k:
            c=1
            ans+=1
            t=a[i]+d+w
        c+=1

    print(ans)