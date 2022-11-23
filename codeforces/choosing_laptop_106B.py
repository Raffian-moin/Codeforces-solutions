n = int(input())

laptops =[[1, 2, 3, 4], [2, 3, 4, 5], [1, 2, 34, 3]]

# while n:
#     laptops.append(list(map(int,input().split())))
#     n = n-1

# for index, value in enumerate(laptops):
#     for index, value in enumerate(laptops)

my_list = {}
min = 0
for index in range(len(laptops)):
    my_list[index] = laptops[index]
    for index2 in range(len(laptops)):
        if index != index2:
            if laptops[index][0] < laptops[index2][0] and laptops[index][1] < laptops[index2][1] and laptops[index][2] < laptops[index2][2]:
                del my_list[index]
for x in my_list:
  print(thisdict[x])
print(my_list)