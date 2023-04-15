for _ in range(int(input())):
    n=int(input())
    s=int(input())

    if len(str(int('1'*(n+1))-s)) > n:
        print(int('9'*n)-s)
    else:
        print(int('1'*(n+1))-s)

# can also be written as
# print (int('1'*(l+1) if n[0]=='9' else '9'*l)-int(n))