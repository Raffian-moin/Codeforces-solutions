# make it optimized removing nested loop
n = int(input())
input = input()
target = "ACTG"
l =[]

for ch in input:
    arr = []

    for ch2 in target:
        if abs(ord(ch) - ord(ch2)) >= 14 and ord(ch) >= ord('O'):
            arr.append(abs(ord(ch) - ord('Z')) +1+abs(ord('A')-ord(ch2)))
        elif abs(ord(ch) - ord(ch2)) >= 14 and ord(ch) < ord('O'):
            arr.append(abs(ord(ch) - ord('A')) +1+abs(ord('Z')-ord(ch2)))
        else:
            arr.append(abs(ord(ch) - ord(ch2)))
    l.append(arr)

num = []

for index in range(len(l)-3):
    num.append(l[index][0]+l[index+1][1]+l[index+2][2]+l[index+3][3])
num.sort()
print(num[0])