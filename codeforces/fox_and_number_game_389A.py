n = int(input())
l = list(map(int, input().split()))
def findDiff():
    count = 1
    for index in range(1, len(l)):
        if l[index] > l[index-1]:
            l[index] = l[index] - l[index-1]
            
        elif l[index-1] > l[index]:
            l[index-1] = l[index-1] - l[index]
        else:
            count = count+1
    if count < len(l):
        return findDiff()
    else:
        return



findDiff()
sum = 0
for index in range(len(l)):
    sum = sum+l[index]

print(sum)

# Better Solution
# greatest common divisor
# import math
# n=int(input())
# l=map(int,input().split())
# a=0
# for i in l:
#     a=math.gcd(a,i)
# print(a*n)