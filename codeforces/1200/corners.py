import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m=list(map(int, input().split()))
    one=0
    a=[]
    ans=0
    flag=0

    for _ in range(n):
        x=input().strip()
        one+= x.count('1')
        a.append(list(x))
    

    for i in range(n-1):
        for j in range(m-1):
            if int(a[i][j]) + int(a[i][j+1]) +  int(a[i+1][j]) + int(a[i+1][j+1]) < 3:
                flag=1
                break
    if one==n*m:
        ans=n*m-2
    elif one==0:
        ans=0
    elif flag==1:
        ans=one
    else:
        ans=one-1
    print(ans)