for _ in range(int(input())):
    n=int(input())
    a = list(map(int, input().split()))
    v= {}
    for i in range(n-1, -1, -1):
        v[a[i]]=i

    for i in range(n-1, 0, -1):
        if (a[i] > a[i-1]  and i > v[a[i]])  or a[i] < a[i-1]:
            print(len(set(a[:i])))
            break
    else:
        print(0)