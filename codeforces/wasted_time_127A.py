import math
inputs = list(map(int,input().split()))

coordinate_numbers = inputs[0]
signature_number = inputs[1]

coordinates = []

total_length = 0

for _ in range(coordinate_numbers):
    coordinate = list(map(int,input().split()))
    coordinates.append(coordinate)

for index, value in enumerate(coordinates):
    if index < len(coordinates) - 1:
        length = math.sqrt(pow((coordinates[index][0] - coordinates[index+1][0]), 2) + pow((coordinates[index][1] - coordinates[index+1][1]), 2))
        total_length = total_length + length

print((total_length/50) *signature_number)