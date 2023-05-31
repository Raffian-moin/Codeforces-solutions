for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    print(n-1)
    if n>1:
        print(1, n)

        if (a[0]+a[-1])%2==1:
            a[-1]=a[0]
        else:
            a[0]=a[-1]

        for i in range(1, n-1):
            if (a[i]+a[0])%2==1:
                print(1, i+1)
            else:
                print(i+1, n)