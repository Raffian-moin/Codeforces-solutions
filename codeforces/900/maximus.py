n=int(input())
a=list(map(int, input().split()))
m=a[0]

for i in range(1, n):
    a[i]=m+a[i]
    m=max(m, a[i])
print(*a)