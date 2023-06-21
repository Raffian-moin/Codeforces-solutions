for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    s=0
    c=0
    flag=False
    for i in range(n):
        s+=abs(a[i])
        if a[i]<0 and flag==False:
            flag=True
            c+=1
        elif a[i]>0:
            flag=False

    print(s, c)
