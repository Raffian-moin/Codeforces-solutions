for _ in range(int(input())):
    n=int(input())
    start=1
    while start<=n:
        d=1
        while (start*d<=n):
            print(start*d, end=" ")
            d*=2
        start+=2
    print()

