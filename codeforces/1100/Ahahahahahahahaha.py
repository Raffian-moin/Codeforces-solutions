for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    if sum(a)%2==1:
        a.remove(1)

    x=False
    p=-1
    b=[]
    for i in range(len(a)):
        if a[i]==0:
            b.append(0)
        elif x==False:
            b.append(1)
            x=True
            p=i+1
        elif p%2!=i%2:
            b[-1]=1
            p=i+1
        else:
            b.append(1)
            p=i+1
    print(len(b))
    print(*b)

# Efficient solution
# for _ in range(int(input())):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     x=arr.count(0)
#     if x>=n//2:
#         out=[0]*x
#     else:
#         out=[1]*((n-x)//2)*2
#     print(len(out))
#     print(*out)