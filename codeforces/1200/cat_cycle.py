for _ in range(int(input())):
    n,k=list(map(int, input().split()))

    if n%2==1:
        k= k+ (k-1)//((n-1)//2)

    print(n if k%n==0 else k%n)