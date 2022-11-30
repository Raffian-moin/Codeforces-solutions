n = int(input())
l = list(map(int, input().split()))
count = 0
for i in range(n):
    if l[i] == 25:
        count=count+1
    else:
        count = count-(int(l[i]/25)-1)
        if count<0:
            break

if count >= 0:
    print('YES')
else:
    print('NO')