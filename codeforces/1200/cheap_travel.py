n,m,a,b=list(map(int, input().split()))

print(min((n//m)*b+min(b, (n%m)*a), n*a))