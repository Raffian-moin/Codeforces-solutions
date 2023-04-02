n=int(input())
a=list(map(int, input().split()))
b=sorted(a)
c=[-1, -1]
 
for i in range(n):
    if a[i]!=b[i]:
        if c[0]==-1:
            c[0]=i
        else:
            c[1]=i
 
d=a[c[0]:c[1]+1][::-1]
 
if c[0]==-1:
    print('yes')
    print(1, 1)
elif a[:c[0]]+d+a[c[1]+1:]==b:
    print('yes')
    print(c[0]+1, c[1]+1)
else:
    print('no')

# condition can also be written as 
# if c[0]==-1:
#     print('yes')
#     print(1, 1)
# elif list(reversed(a[c[0]:c[1]+1]))==b[c[0]:c[1]+1]:
#     print('yes')
#     print(c[0]+1, c[1]+1)
# else:
#     print('no')