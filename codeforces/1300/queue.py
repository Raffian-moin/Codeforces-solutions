n=int(input())
a=list(map(int, input().split()))
a.sort()
c=1
s=a[0]
for i in range(1, n):
    if a[i]>=s:
        s+=a[i]
        c+=1
print(c)