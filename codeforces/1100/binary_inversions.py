for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    one=0
    zero=0
    c=0
    r=0
    l=0

    for i in range(n):
        if a[i]==0:
            zero+=1
            c+=one
            if zero==1:
                l=i
        else:
            one+=1
            r=i+1

    print(max(c+one-1-(n-r), c, c+zero-1-l))
    