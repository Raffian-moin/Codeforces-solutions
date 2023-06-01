for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    for el in a:
        print(n-el+1, end=' ')
    print()