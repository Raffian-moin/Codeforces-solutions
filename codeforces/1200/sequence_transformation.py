import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    d={a[0]:1}

    for i in range(1,n):
        if a[i]!=a[i-1] and a[i] not in d:
            d[a[i]]=1
        elif a[i]!=a[i-1]:
            d[a[i]]+=1
    d[a[0]]-=1
    d[a[-1]]-=1

    print(min(d.values())+1)