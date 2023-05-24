import sys
input = sys.stdin.readline
from collections import defaultdict
for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    b=sorted(list(map(int, input().split())))
    c=sorted(a)
    orDict = defaultdict(list)

    for i in range(n):
        orDict[c[i]].append(b[i])

    for i in range(n):
        b[i]=orDict[a[i]][-1]
        orDict[a[i]].pop()

    print(*b)