import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m=list(map(int, input().split()))
    a=[]
    for i in range(n):
        a.append(list(map(int, input().split())))

    z=0
    for i in range((n+1)//2):
        
        for j in range((m+1)//2):
            x = sorted([a[i][j],a[i][m-j-1],a[n-i-1][j],a[n-i-1][m-j-1]])
            p = abs(x[0]-x[2])+abs(x[1]-x[2])+abs(x[3]-x[2])
            if m%2==1 and j+1==(m+1)//2 or n%2==1 and i+1==(n+1)//2:
                p=p//2
            z+= p

    print(z)