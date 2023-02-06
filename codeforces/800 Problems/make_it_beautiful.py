a = list(map(int, input().split()))
a.sort()

start = 0
end = len(a)-1
new_array = []

for i in range(1, len(a)+1):
    if start <= end:
        if i%2==1:
            new_array.append(a[start])
            start = start+1
        else:
            new_array.append(a[end])
            end = end-1

print(*new_array)