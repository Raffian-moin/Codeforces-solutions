n,l=list(map(int, input().split()))
a=list(map(int, input().split()))
a.sort()
m=max((a[0]-0)*2, (l-a[n-1])*2)
for i in range(n-1):
    m=max(m, a[i+1]-a[i])

print(f'{m/2:.10f}')

# formuala can also be
# max(m/2, a[0]-0, l-a[n-1])