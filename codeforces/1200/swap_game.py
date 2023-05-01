for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    if min(a)==a[0]:
        print('Bob')
    else:
        print('Alice')