from operator import itemgetter
n=int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
b = sorted(arr, key=itemgetter(0))

m = b[n-1][1]

for i in range(n-2, -1, -1):
    if b[i][1] > m and b[i][0] < b[i+1][0]:
        print('Happy Alex')
        break
    else:
        m=min(m, b[i][1])
else:
    print('Poor Alex')

# optimized solution

# for i in range(input()):
# 	a,b=raw_input().split()
# 	if a!=b:print "Happy Alex";exit()
# print "Poor Alex"