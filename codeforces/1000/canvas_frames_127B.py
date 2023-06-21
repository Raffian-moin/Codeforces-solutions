import math
n = int(input())
sticks = list(map(int,input().split()))

sticks.sort()
 
pair = 0
count = 1

for index in range(len(sticks)-1):
    if sticks[index] == sticks[index+1]:
        count = count + 1
        if index == len(sticks)-2:
            pair = pair + math.floor(count/2) 
    else:
        pair = pair + math.floor(count/2) 
        count = 1

frames = math.floor(pair/2)

print(frames)