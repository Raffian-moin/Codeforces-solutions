import sys
input = sys.stdin.readline
n,k,x=list(map(int, input().split()))
a=sorted(list(map(int, input().split())))
b=[]
c=1
for i in range(1,n):
    if a[i]-a[i-1]>x:
        b.append(a[i]-a[i-1])
        c+=1

b.sort()
d=0
while(k>0 and d<len(b)):
    z=((b[d]+x-1)//x)-1
    if z<=k:
        k-=z
        c-=1
    d+=1

print(c)