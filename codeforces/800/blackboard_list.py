for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()

    print(a[0] if a[0]<0 else a[-1])