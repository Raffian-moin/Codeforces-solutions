for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    if a.count(0)-(n-a.count(0)) < 2:
        print(0)
    elif a.count(0)-(n-a.count(0)) >1 and max(a)!=1:
        print(1)
    else:
        print(2)