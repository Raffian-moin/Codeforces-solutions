for _ in range(int(input())):
    s=input()
    if len(set(s))==1:
        print(s)
    else:
        x=0
        for i in range(len(s)*2):
            if x==0:
                x=1
            else:
                x=0
            print(x, end="")
        print()

        # else condition can also be written as
        # "10"*len(s)


