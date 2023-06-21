for _ in range(int(input())):
    n=int(input())
    print((n+1)//2)

    l=1
    r=n*3
    for i in range(n//2):
        print(l, r)
        l+=3
        r-=3

    if n%2==1:
        print((n//2*3)+1, 3*(n+1)//2)

# can also be solve by this 
# print(1+3*i, 3*n-3*i)