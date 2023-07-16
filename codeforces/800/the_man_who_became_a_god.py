for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    b=[]

    for i in range(1, n):
        b.append(abs(a[i]-a[i-1]))

    b.sort(reverse=True)
    print(sum(b[k-1:]))