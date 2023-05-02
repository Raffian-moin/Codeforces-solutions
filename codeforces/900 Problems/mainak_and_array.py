for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    m=max(a[-1]-a[0], max(a)-a[0], a[-1]-min(a))

    for i in range(n-1):
        m=max(m, a[i]-a[i+1])

    print(m)