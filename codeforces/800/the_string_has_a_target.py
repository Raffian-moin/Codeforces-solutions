for _ in range(int(input())):
    n=int(input())
    s=input()
    index=-1
    first=ord(s[0])

    for i in range(n):
            order=ord(s[i])
            if order<=first:
                first=order
                index=i

    # we don't need this if condition as 
    # index will be always greater than -1
    if index>-1:
        s=s[index]+s[:index]+s[index+1:]
    print(s)