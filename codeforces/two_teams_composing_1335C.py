t = int(input())

while t:
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    count = 1
    maximum = 1
    dis = n
    for i in range(n-1):
        if l[i] == l[i+1]:
            count = count+1
            maximum = max(count, maximum) 
            dis = dis-1
        else:
            count = 1
    print(max(min(maximum-1, dis), min(maximum, dis-1)))
    t = t-1
