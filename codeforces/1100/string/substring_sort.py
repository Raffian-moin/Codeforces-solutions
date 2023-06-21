n=int(input())
a=[]
for i in range(n):
    s=input()
    a.append([len(s), s])
a.sort(key=lambda x: x[0])
flag=0
for i in range(n-1):
    if a[i][1] not in a[i+1][1]:
        flag=1
        break

if flag==1:
    print('NO')
else:
    print('YES')
    for i in range(n):
        print(a[i][1])

# elegant answer
# a = [input() for _ in range(n)]
# a.sort(key=len)
# if all(a[i] in a[i+1] for i in range(n-1)):
#     print("YES")
#     print(*a, sep='\n')
# else:
#     print("NO")