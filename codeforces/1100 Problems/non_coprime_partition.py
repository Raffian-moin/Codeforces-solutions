n=int(input())
if n<=2:
    print('No')
else:
    print('Yes')
    print(1, n)
    print(n-1, end = ' ')
    arr=[]
    for i in range(1, n):
        print(i, end = ' ')

# can also be written as for space separated value print
# print(n-1,*range(1,n))
