l = list(map(int, input().split()))
l.sort()
count = 0
even =0
odd =0
print(l)
for i in range(len(l)-1, -1, -2):
    if abs(l[i] - l[i-1]) ==1 or l[i]%2 == l[i-1]%2:
        count = count+1
    if l[i] %2==0:
        even = even+1
    else:
        odd = odd+1
    if l[i-1]%2==0:
        even = even+1
    else:
        odd = odd+1
print(even, odd)
if even%2 ==0 and odd%2==0:
    print('YES')
elif count ==len(l)/2:
    print('YES')
else:
    print('NO')
