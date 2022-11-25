n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
pointer = 1
maximum = 1
for index in range(len(l)-1):
    if l[index] != l[index+1]:
        pointer = pointer+1
        maximum = max(pointer, maximum)
    else:
        pointer = 1

print(maximum)

