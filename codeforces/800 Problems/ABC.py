for _ in range(int(input())):
    n=int(input())
    s=input()
    x=[int(x) for x in s]

    if n==1:
        print('YES')
    elif n==2 and len(set(x))==2:
        print('YES')
    else:
        print('NO')