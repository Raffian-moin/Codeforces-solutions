for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    print(a[n-1]*a[n-2] if a[n-1]*a[n-2]> a[0]*a[1] else a[0]*a[1])

    # can also be written as
    # print(max(a[0] * a[1], a[-1] * a[-2]))