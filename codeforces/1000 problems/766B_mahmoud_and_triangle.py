n = int(input())
arr = list(map(int, input().split()))

arr.sort()

for i in range(1, n-1):
    if arr[i-1]+arr[i] > arr[i+1]:
        print('YES')
        break
else:
    print('NO')
