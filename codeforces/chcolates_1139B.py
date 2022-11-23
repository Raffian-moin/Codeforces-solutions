list = [3, 2, 5, 4, 10]

# for index, value in enumerate(list):
count = 0
for index in range(len(list)-1):
    if index == len(list)-2:
        count = count + list[index+1]

    if index <= list[index] and list[index+1] - list[index] > 0:
        count = count + list[index]
    elif index <= list[index] and list[index+1] - list[index] < 0:
        count = 0
        count = count + (list[index+1]-1)

print(count)