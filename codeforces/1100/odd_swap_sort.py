import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    odd=0
    even=0

    for el in a:
        if el&1 and el<odd:
            print('No')
            break
        elif el&1:
            odd=el
        elif el<even:
            print('No')
            break
        else:
            even=el
    else:
        print('Yes')

    # Elegant approach
    # f=[0, 0]
    # for el in a:
    #     if f[el&1] > el:
    #         print('No')
    #         break
        
    #     f[el&1]=el
    # else:
    #     print('Yes')