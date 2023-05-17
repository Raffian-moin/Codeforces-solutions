import sys
input = sys.stdin.readline
from itertools import accumulate
n,q,k=list(map(int, input().split()))
a=list(map(int, input().split()))

a.insert(0, 0)
a.append(k)
b = [0]

for i in range(1, n+1):
    b.append(max(0, a[i+1]-a[i-1]-2))

c=list(accumulate(b))

for _ in range(q):
    l,r=list(map(int, input().split()))
    x=c[r]-c[l-1]+a[l-1]
    if a[r]!=k:
        x+=k-a[r+1]+1
    print(x)