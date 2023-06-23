for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=sorted(a)

    if b==a:
        print(0)
    elif a[-2]>a[-1] or a[-1]<0 and a[-2]<0:
        print(-1)
    else:
        print(n-2)
        for i in range(n-2):
            print(i+1, n-1, n)