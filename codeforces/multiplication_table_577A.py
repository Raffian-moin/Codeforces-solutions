n= int(input())
target=int(input())

arr = []
count = 0
for i in range(n):
    arr.append(i+1)

print(arr)

for i in range(n):
    div = int(target/(i+1))
    print(div)
    if div in arr:
        arr.remove(div)
        count = count+2

print(count)