for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    s=0
    flag=0
    for i in range(n):
        if a[i]<= 2048:
            s+=a[i]
            if s>=2048:
                flag=1
                break
                
    print('YES' if flag==1 else 'NO')

        