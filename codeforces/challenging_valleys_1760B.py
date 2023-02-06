points = [3, 2, 2, 1, 2, 2, 3]
valley = 0
l=0
r=0
for i in range(len(points)):
    if i == 0 and points[i] < points[i+1]:
        valley = valley+1
    if i == len(points)-1 and points[i] > points[i-1]:
        valley = valley+1
    if i <0 and i<len(points)-1:
        if points[i] > points[i-1] and points[i] == points[i+1]:
            l=i
            r=i+1

if valley ==1:
    print('YES')
else:
    print('NO')