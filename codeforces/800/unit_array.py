for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    neg=0
    s=sum(a)
    ans=0
    for el in a:
        if el<0:
            neg+=1

    if s<0:
        ans=(abs(s)+1)//2
        if neg%2!=ans%2:
            ans+=1
    elif neg%2==1:
        ans=1
    print(ans)

