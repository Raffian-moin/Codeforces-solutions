for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    if n%2==1:
        print(-1)
        continue
    
    s=sum(a)
    m=abs(s)//2
    print(m+n-abs(s))
    i=0
    while i<n:
        if m>0 and a[i]+a[i+1]== -2 and s<0:
            print(i+1, i+2)
            m-=1
            i+=2
        elif m>0 and a[i]+a[i+1]== 2 and s>0:
            print(i+1, i+2)
            m-=1
            i+=2
        else:
            print(i+1, i+1)
            i+=1
