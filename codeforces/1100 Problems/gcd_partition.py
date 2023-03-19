import math
for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    m=0
    for i in range(1, n):
        a[i]=a[i-1]+a[i]

    for i in range(n-2, -1, -1):
        m=max(math.gcd(a[-1], a[i]), m)
    
    print(m)
