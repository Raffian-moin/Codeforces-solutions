n=int(input())
a=sorted(list(map(int, input().split())))
m=int(input())
b=sorted(list(map(int, input().split())))
c=a+b[::-1]


l=0
r=n+m-1
d=0
while (l<n and r>=n):
    if abs(c[r]-c[l]) in [0,1]:
        d+=1
        l+=1
        r-=1
    elif c[r]>c[l]:
        l+=1
    else:
        r-=1

print(d)

# can also be written as:
# don't need to use concatenate two arrays
# i,j,k=0,0,0
# while i<n and j<m:
# 	if abs(a[i]-b[j])<2:
#         k+=1;
#         i+=1;
#         j+=1
# 	elif a[i]<b[j]:
#         i+=1
# 	else:j+=1
# print(k)