for _ in range(int(input())):
    a = input()
    b = input() 

    if a[0] == b[0]:
        print('YES')
        print(a[0]+'*')
    elif a[len(a)-1] == b[len(b)-1]:
        print('YES')
        print('*'+a[len(a)-1])
    else:
        for i in range(len(a)-1):
            if a[i:i+2] in b:
                print('YES')
                print('*'+a[i:i+2]+'*')
                break
        else:
            print('NO')

# for last index in python
# a[-1] works
# a[len(a)-1] == b[len(b)-1] can also be written as 
# a[-1] == b[-1]