n=int(input())
m=0
arr=[]
for i in range(n):
    a=list(map(int, input().split()))
    m=0
    for b in a:
        m=max(m, a.count(b))

    if m > 1:
        arr.append(n-m)
    elif n not in arr:
        arr.append(n)
    else:
        arr.append(n-1)

print(*arr)

# can also be written as 
# n = int(input())
# A = [list(map(int, input().split())) for i in range(n)]
 
# ans = [max(row) for row in A]

# here find the index of n-1 replace the n-1 value with n because n-1 occurs twice
# ans[ans.index(n-1)] = n
# print(*ans)