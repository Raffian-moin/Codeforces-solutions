for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    ans=[]
    x=0

    for i in range(1, n+1):
        if a[i-1]!=b[i-1]:
            x+=3
            ans+=[i, 1, i]

    print(*([x]+ans))