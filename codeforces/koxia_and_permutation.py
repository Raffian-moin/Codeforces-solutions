n, m = input().split()
c = int(n)-int(m)+1
arr = []
for i in range(1, int(n)+1):
    arr.append(i)

new_arr = []
last = len(arr)-1
first = 0
flag = 0
for i in range(len(arr)):
    if flag ==1:
        break
    new_arr.append(arr[last])
    last = last-1
    
    for j in range(c-1):
        # print(last)
        if last==first:
            flag = 1
            break
        else:
            new_arr.append(arr[first])
            first=first+1

print(new_arr)
