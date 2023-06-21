import math
n , d = list(map(int,input().split()))
arr = list(map(int,input().split()))

arr.sort()
low = -1
high = len(arr)-1
sum = 0

while high>low:
    low += math.ceil((d+1)/arr[high])-1
    high-= 1
    if high < low:
        break
    else:
        sum+=1

print(sum)