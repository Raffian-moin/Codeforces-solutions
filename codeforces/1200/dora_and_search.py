for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    l,r=0, n-1
    s,h=1,n
    flag=0

    while(l<r):
        if a[l]==s:
            l+=1
            s+=1
        elif a[l]==h:
            l+=1
            h-=1
        elif a[r]==s:
            r-=1
            s+=1
        elif a[r]==h:
            r-=1
            h-=1
        else:
            flag=1
            break

    if flag==0:
        print(-1)
    else:
        print(l+1, r+1)