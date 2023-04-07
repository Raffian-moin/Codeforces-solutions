n=list(map(int, input()))
index=-1
for i in range(len(n)-1):
    if n[i]%2==0:
        index=i
        if n[-1]>n[i]:
            break

if index==-1:
    print(-1)
else:
    n[index], n[-1]=n[-1], n[index]
    print(''.join(map(str, n)))
