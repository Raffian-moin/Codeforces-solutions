for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    b=[]
    x=n-1
    c=x

    while(x>0):
        b.append(a[c-1])
        x-=1
        c+=x

    print(*(b+[a[-1]]))