import sys
from itertools import accumulate
input = sys.stdin.readline
for _ in range(int(input())):
    n,q=list(map(int, input().split()))
    a=list(map(int, input().split()))
    a=list(accumulate(a))
    a.insert(0, 0)

    for i in range(q):
        l,r,k=list(map(int, input().split()))
        if (a[-1]-(a[r]-a[l-1])+(r-l+1)*k)%2==1:
            print('YES')
        else:
            print('NO')

