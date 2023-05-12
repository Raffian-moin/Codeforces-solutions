import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m=list(map(int, input().split()))
    a=list(map(int, input().split()))
    c=0
    b={}

    for el in a:
        if el%m in b:
            b[el%m]+=1
        else:
            b[el%m]=1

    for x in b:
        if x==0 or x==m/2:
            c+=1
        elif m-x in b and max(b[x],b[m-x])>0:
            c+=max(abs(b[x]-b[m-x]), 1)
            b[x]=0
            b[m-x]=0
        else:
            c+=b[x]
    print(c)

    
