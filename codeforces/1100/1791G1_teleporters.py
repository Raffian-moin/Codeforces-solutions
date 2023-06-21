for _ in range(int(input())):
    n, c = list(map(int, input().split()))
    a = list(map(int, input().split()))

    for i in range(n):
        a[i]=a[i]+i+1

    a.sort()
    s=0

    for i in range(n):
        s+=a[i]
        if s > c:
            print(i)
            break
    else:
        print(i+1)