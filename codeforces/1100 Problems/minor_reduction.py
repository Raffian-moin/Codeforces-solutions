for _ in range(int(input())):
    a=list(map(int, input()))
    for i in range(len(a)-1, 0, -1):
        if a[i]+a[i-1] >= 10:
            # can also be written as
            # x[i] += x[i-1] - 10
            # x[i-1] = 1
            print(''.join(map(str, a[:i-1]+ [a[i]+a[i-1]]+a[i+1:])))
            break
    else:
        # can also be written as
        # x[1] += x[0]
        # x.pop(0)
        print(''.join(map(str, [a[0]+a[1]]+a[2:])))
        
# can also be written as
# print(''.join(map(str, a)))