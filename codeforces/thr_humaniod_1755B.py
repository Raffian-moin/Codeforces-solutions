# import math
# astronauts, humanoid_power = list(map(int,input().split()))
# astronauts_power = list(map(int,input().split()))

# astronauts_power.sort()

green_serum = 2
blue_serum = 1
humanoid_power = 2

# for index, value in enumerate(astronauts_power):
#     if humanoid_power > value:
#         # del astronauts_power[index]
#         humanoid_power = humanoid_power + math.floor(value/2)
#     elif humanoid_power <= value and green_serum != 0 and blue_serum != 0:
#         humanoid_power = humanoid_power*2
#         if humanoid_power < value and green_serum != 0 and blue_serum != 0:
#             green_serum = green_serum - 1
#             # del astronauts_power[index]
#             humanoid_power = humanoid_power + math.floor(value/2)
#             print(humanoid_power)
#     if index == 1:
#         break

# # print(humanoid_power)
# print(astronauts_power)

def multiplyPower(humanoid_power, value):
    global green_serum
    global blue_serum
    if (green_serum == 0 and blue_serum == 0):
        return humanoid_power
        
    if humanoid_power <= value and green_serum != 0:
        humanoid_power = humanoid_power* 2
        green_serum = green_serum - 1
        if humanoid_power <= value:
            return multiplyPower(humanoid_power, value)
    elif humanoid_power <= value and blue_serum != 0:
        humanoid_power = humanoid_power * 3
        blue_serum = blue_serum - 1
        if humanoid_power <= value:
            return multiplyPower(humanoid_power, value)

result = multiplyPower(1, 6)
print(result)