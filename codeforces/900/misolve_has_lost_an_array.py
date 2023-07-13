n,l,r=list(map(int, input().split()))
mi=1
ma=1
x=1
y=1
for i in range(l-1):
    mi+=x*2
    x*=2

for i in range(r-1):
    ma+=y*2
    y*=2

print(mi+(n-l)*1, ma+(n-r)*y)