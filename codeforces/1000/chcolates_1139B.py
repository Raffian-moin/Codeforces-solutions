n = int(input())
arr = list(map(int, input().split()))

maximum = arr[n-1]
total = maximum

for i in range(n-2, -1, -1):
    maximum = min(maximum-1, arr[i])
    if maximum > 0:
        total+= maximum

print(total)

