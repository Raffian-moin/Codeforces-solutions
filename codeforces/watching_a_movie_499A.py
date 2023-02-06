n, x = list(map(int, input().split()))
# l =[]
pre_min = 0
total_min = 0
while n:
    l, r = list(map(int, input().split()))
    if l !=1:
        if l%x == 0:
            total_min = total_min + r - ((l/x)-1)*x
    n = n-1

print(total_min)