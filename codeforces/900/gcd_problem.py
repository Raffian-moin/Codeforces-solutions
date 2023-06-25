for _ in range(int(input())):
    n=int(input())

    if n%2==1 and ((n-1)//2)%2==1:
        print((n+3)//2,  (n-4)//2, 1)
    elif n%2==1:
        print((n+1)//2,  (n-2)//2, 1)
    else:
        print(n//2, (n-2)//2, 1)
    