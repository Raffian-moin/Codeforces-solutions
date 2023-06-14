import sys
input = sys.stdin.readline
import bisect
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    x=[]
    m=0
    for i in range(n):
        if a[i] < i+1:
            m+=bisect.bisect_left(x, a[i])
            x.append(i+1)
    print(m)