from itertools import accumulate
import bisect
for _ in range(int(input())):
    n,q=list(map(int, input().split()))
    a=[0]+list(map(int, input().split()))
    b=list(map(int, input().split()))
    d=list(accumulate(a))
    x=-1
    c=[]
    for el in a:
        if el>x:
            x=el
        c.append(x)

    for val in b:
        print(d[bisect.bisect_right(c, val)-1], end=" ")
    print()