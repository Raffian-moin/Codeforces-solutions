import sys
input = sys.stdin.readline
from itertools import accumulate
import bisect

for _ in range(int(input())):
    n,m,h=list(map(int, input().split()))
    a=[]
    pos=1
    problem=0
    time=0
    for i in range(n):
        a+=[sorted(list(map(int, input().split())))]
        if i==0:
            x=list(accumulate(a[0]))
            y=list(accumulate(x))
            problem=bisect.bisect_right(x, h)
            time=y[problem-1]

    for el in a:
        x=list(accumulate(el))
        y=list(accumulate(x))
        index=bisect.bisect_right(x, h)
        if index>problem:
            pos+=1
        elif index==problem and problem!=0 and y[index-1]<time:
            pos+=1

    print(pos)
            