import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    c=0
    x=a[0]*2-1
    for i in range(1, n):
        c+=math.ceil(a[i]/x)-1
    print(c)
