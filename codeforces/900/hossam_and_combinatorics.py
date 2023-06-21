for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()

    if a[-1]==a[0]:
        print(n*(n-1))
        # can also be written as
        # print(n*n-n)
    else:
        print(a.count(a[-1])*a.count(a[0])*2)
