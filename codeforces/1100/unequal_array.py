for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    l=0
    r=0

    for i in range(n-1):
        if l==0 and a[i]==a[i+1]:
            l=i+1
        elif a[i]==a[i+1]:
            r=i

    if l>0 and r>0:
        print(max(r-l, 1))
    else:
        print(0)

