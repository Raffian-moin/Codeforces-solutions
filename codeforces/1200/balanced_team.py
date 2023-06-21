import sys
input = sys.stdin.readline
n=int(input())
a=list(map(int, input().split()))
a.sort()
x=0
m=0

for i in range(n):
    if a[i]-a[x]<=5:
        m=max(m, i-x+1)
    else:
        x+=1
print(m)