import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    s=list(input())
    b=[]
    r=[]
    flag=True

    for i in range(n):
        if s[i]=='B':
            b.append(a[i])
        else:
            r.append(a[i])

    b.sort()
    r.sort()

    c=1
    for i in range(len(b)):
        if b[i]<c:
            flag=False
            break
        c+=1

    p=n-len(r)+1
    for j in range(len(r)):
        if r[j]>p:
            flag=False
            break
        p+=1

    print('NO' if flag==False else 'YES')