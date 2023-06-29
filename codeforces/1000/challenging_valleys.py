for _ in range(int(input())):
    n=int(input())
    a=[1e9+1]+list(map(int, input().split()))+[1e9+1]
    c=0
    l=0

    for i in range(1, n+1):
        if a[i]!=a[i-1]:
            l=a[i-1]
        if l>a[i] and a[i]<a[i+1]:
            c+=1

    print('YES' if c==1 else 'NO')
