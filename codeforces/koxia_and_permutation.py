for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    r=0
    l=1
    for i in range(1, n+1):
        if i%2==1:
            print(n-r, end=" ")
            r+=1
        else:
            print(l, end=" ")
            l+=1
    print()

# can also be written as 
# for i in range(n//2):
# print(n-i, i+1, end=' ')
# print(n//2+1 if n & 1 else '')
