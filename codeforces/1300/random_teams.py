n, m=list(map(int, input().split()))
x=n//m
print(m*x*(x-1)//2+x*(n%m), (n+1-m)*(n-m)//2)