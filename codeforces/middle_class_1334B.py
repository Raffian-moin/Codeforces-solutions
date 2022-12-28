l = list(map(int, input().split()))
k = 5
l.sort()
sum = 0
n = 0
count = 0


for i in range(len(l)-1, -1, -1):
    sum = sum+l[i]
    n=n+1
    if sum/n >= k:
        count = count+1
    else:
        break

print(count)
