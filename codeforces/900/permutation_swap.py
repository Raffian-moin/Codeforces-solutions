import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    m=0

    for i in  range(n):
        if a[i]!=i+1:
            m=math.gcd(m, abs(a[i]-(i+1)))

    print(m)