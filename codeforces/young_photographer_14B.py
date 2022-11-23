n, x = list(map(int, input().split()))

left = []
right = []
new_list = []

while n:
    a, b = list(map(int, input().split()))
    
    if a>b:
        min = b
        max = a
    else:
        min = a
        max = b
    left.append(x-min)
    right.append(max-x)
    new_list.append([min, max]) 
    n = n-1

left.sort()
right.sort()
count = 0
print(new_list)
for index in range(len(new_list)):
    if left[0] < 0:
        if new_list[index][0]+abs(left[0]) > new_list[index][1]:
            count = -1
            break
        else:
            count = abs(left[0])
    elif right[0] < 0:
        if new_list[index][1]+abs(right[0]) > new_list[index][0]:
            count = -1
            break
        else:
            count = abs(right[0])

print(count)
print(right)
print(left)

# 10 16
# 4 18
# 6 19
# 22 1
# 23 0
# 1 22
# 9 22
# 4 19
# 0 14
# 6 14
# 0 16