import math
for _ in range(int(input())):
    n, x=list(map(int, input().split()))
    a=list(map(int, input().split()))
    c=0
    for i in range(n):
        c+=math.ceil(a[i]/x)
    print(int(math.ceil(sum(a)/x)), int(c))