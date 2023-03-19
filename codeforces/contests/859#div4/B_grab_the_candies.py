for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    e=0
    o=0
    for el in a:
        if el%2==0:
            e+=el
        else:
            o+=el

    print('YES' if e>o else 'NO')