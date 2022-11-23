n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))
new_array = []

for index in range(n):
    new_array.append(arr[index])

for index in range(k):
    del new_array[0]
    new_array.append(0)
    
print(new_array)
