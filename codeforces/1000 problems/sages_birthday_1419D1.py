n = int(input())
arr = list(map(int, input().split()))

arr.sort()
left = arr[:n//2]
right = arr[n//2:]

a = []

for i in range(len(right)):
    a.append(right[i])
    if i+1 <= len(left):
        a.append(left[i])

print((n-1)//2)
print(*a)