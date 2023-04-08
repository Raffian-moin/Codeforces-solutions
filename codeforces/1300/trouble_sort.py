for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    if a==sorted(a):
        print('Yes')
    elif len(set(b))==2:
        print('Yes')
    else:
        print('No')