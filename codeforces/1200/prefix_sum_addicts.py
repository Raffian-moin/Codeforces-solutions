import sys
for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    x=sys.maxsize
    flag=True

    for i in range(len(a)-1, 0, -1):
        if a[i]-a[i-1]>x:
            flag=False
            break
        x=a[i]-a[i-1]

    if flag==False or a[0]/(n-k+1) > x:
        print('NO')
    else:
        print('YES')