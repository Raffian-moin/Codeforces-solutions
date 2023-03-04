for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a.sort()

    c = 0
    extra = 0

    for i in range(n-1, -1, -1):
        if a[i] >= x:
            c+=1
            extra+= a[i]-x
        elif x-a[i] > extra:
            break
        else:
            extra-= x-a[i]
            c+=1

    print(c)

# can also be written as 
# s=0
# 	y=0
# 	for j in range(n):
# 		s+=a[j]
# 		if(s/(y+1)>=x):
# 			y+=1
# 		else:
# 			break
# 	print(y)
