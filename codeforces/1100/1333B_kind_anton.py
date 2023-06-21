for _ in range(int(input())):
    n=int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s=set()
    for i in range(n):
        if a[i]!=b[i]:
            if (a[i]> b[i] and -1 not in s) or (a[i]<b[i] and 1 not in s):
                print('NO')
                break
        s.add(a[i])
    else:
        print('YES') 