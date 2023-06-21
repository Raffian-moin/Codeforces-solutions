for _ in range(int(input())):
    n,a,b=list(map(int, input().split()))
    mid=n//2
    x=[]
    h=n
    l=a
    i=0
    j=0
    p=1
    q=b
    
    if a<=mid and b>mid or mid+1==a and mid==b:
        while(i<mid):
            if h>b:
                x.append(h)
                h-=1
            else:
                x.append(l)
                l+=1
            i+=1
        while(j<mid):
            if p<a:
                x.append(p)
                p+=1
            else:
                x.append(q)
                q-=1
            j+=1

        print(*x)
    else:
        print(-1)


