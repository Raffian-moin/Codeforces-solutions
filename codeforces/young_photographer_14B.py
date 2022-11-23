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
    right.append(x-min)
    left.append(max-x)
    new_list.append([min, max]) 
    n = n-1

right.sort()
left.sort()
count = 0

for index in range(len(new_list)):
    if right[0] < 0:
        if x+abs(right[0]) > new_list[index][1]:
            count = -1
            break
        else:
            count = abs(right[0])
    elif left[0] < 0:
        if x-abs(left[0]) < new_list[index][0]:
            count = -1
            break
        else:
            count = abs(left[0])

print(count)