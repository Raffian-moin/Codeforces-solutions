import sys
from collections import defaultdict
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))+[0]
    b=list(map(int, input().split()))+[0]

    count=defaultdict(int)
    m=0
    x=1
    for i in range(n):
        if a[i]==a[i+1]:
            x+=1
        else:
            count[a[i]]=max(count[a[i]], x)
            x=1
        m=max(m, count[a[i]])

    y=1
    for i in range(n):
        if b[i]==b[i+1]:
            y+=1
        else:
            y=1
        m=max(m, count[b[i]]+y)
    print(m)