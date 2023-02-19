import math

for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(1, n+1):
        arr.append(i)
        
    print(2)
    for i in range(n-1, 0, -1):
        print(arr[i], arr[i-1])
        arr[i-1] = math.ceil((arr[i] + arr[i-1]) /2)