for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    c=0

    for i in range(1, n):
        if a[i]<a[i-1]:
            c+=a[i-1]-a[i]

    print(c)