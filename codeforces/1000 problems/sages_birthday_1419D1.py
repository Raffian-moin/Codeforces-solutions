n = int(input())
arr = list(map(int, input().split()))

arr.sort()
left = arr[:n//2]
right = arr[n//2:]

a = []

for i in range(len(right)):
    a.append(right[i])
    if i <= len(left)-1:
        a.append(left[len(left)-i-1])


print(sum(left[-((n-1)//2):]))
print(*a)