n, x = list(map(int, input().split()))

left = []
right = []
my = {}

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
    my[x-min] = max-x
    n = n-1

left.sort()
right.sort()
count = 0
for key, value in my.items():
    if left[0] < 0:
        if key+abs(left[0]) > value:
            count = -1
            break
        else:
            count = abs(left[0])
    elif right[0] < 0:
        if value+abs(right[0]) > key:
            count = -1
            break
        else:
            count = abs(right[0])

print(count)