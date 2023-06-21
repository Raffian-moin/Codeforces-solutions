import sys
input = sys.stdin.readline
from collections import defaultdict
n=int(input())
a=list(map(int, input().split()))
count=defaultdict(int)

for i in range(n):
    count[a[i]]+=1
    if a[i]==50 and count[25]!=0:
        count[25]-=1
    elif a[i]==100 and count[50]>0 and count[25]>0:
        count[25]-=1
        count[50]-=1
    elif a[i]==100 and count[25]>2:
        count[25]-=3
    elif a[i]!=25:
        print('NO')
        break
else:
    print('YES')
