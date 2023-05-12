for _ in range(int(input())):
    n, c=list(map(str, input().split()))
    n=int(n)
    s=input()

    if c*n==s:
        print(0)
    else:
        for i in range(n//2, n):
            if s[i]==c:
                print(1)
                print(i+1)
                break
        else:
            print(2)
            print(n, n-1)