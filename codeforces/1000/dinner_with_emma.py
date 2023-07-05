n,m=list(map(int, input().split()))
m=1

for _ in range(n):
    m=max(m, min(list(map(int, input().split()))))

print(m)