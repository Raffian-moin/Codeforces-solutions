import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m=list(map(int, input().split()))
    a=[]
    d={}
    for _ in range(n):
        a.append(list(input().strip("")))

    for i in range(n-1, -1, -1):
        for j in range(m):
            if i==n-1:
                d[j]=False

            if a[i][j]=='.' and d[j]==False:
                d[j]=i
            elif a[i][j]=='o':
                d[j]=False

            if a[i][j]=='*' and d[j]!=False:
                a[d[j]][j]='*'
                a[i][j]='.'
                d[j]-=1

    for i in range(n):
        x=''
        for j in range(m):
            x+=a[i][j]
        print(x)