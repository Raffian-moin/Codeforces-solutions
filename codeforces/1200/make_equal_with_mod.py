for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()

    if 1 in a:
        b=list(set(a))
        for i in  range(1, len(b)):
            if b[i] - b[i-1] <=1:
                print('NO')
                break
        else:
            print('YES')
    else:
        print('YES')

# no need to convert to set
# condition could be 
# b[i]==b[i-1]+1
# it will work even  if there are 1,1 
# then 1!== 1+1