for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    flag=False
    odd=0
    for i in range(1, n-1):
        if a[i]>1:
            flag=True
        if a[i]%2==1:
            odd+=1

    if flag==False or (n==3 and a[1]%2==1):
        print(-1)
    else:
        print((sum(a[1:n-1])+odd)//2)