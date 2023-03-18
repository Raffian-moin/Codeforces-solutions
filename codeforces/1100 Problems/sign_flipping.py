for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    arr=[]
    for i in range(n):
        if i%2==0 and a[i] > 0:
            a[i]=a[i]*-1
        elif i%2==1 and a[i] < 0:
            a[i]=a[i]*-1
        arr.append(a[i])

    print(*arr)

# can also be written as 
# k=1
# for i in s.split():print(abs(int(i))*k);k=-k

# first take the absolute value of current element, so it become positive no matter what
# then we either multiply by either k=1 or k=-1