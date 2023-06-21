# revised submission
for _ in range(int(input())):
    n, k=list(map(int, input().split()))
    x=n
    for i in range((n+2)//2):
        if  x*(x-1)/2+(n-x)*(n-x-1)/2==k:
            a=[1]*x
            b=a+[-1]*(n-x)
            print('YES')
            print(*b)
            break

        x-=1
    else:
        print('NO')

# my initial accepted submission
# for _ in range(int(input())):
#     n, k=list(map(int, input().split()))
#     x=n
#     if n==2 and k==0:
#         print('YES')
#         print(-1, 1)
#     else:
#         for i in range((n+2)//2):
#             if (n-x<2 and x*(x-1)/2==k) or x*(x-1)/2+(n-x)*(n-x-1)/2==k:
#                 a=[1]*x
#                 b=a+[-1]*(n-x)
#                 print('YES')
#                 print(*b)
#                 break
#             # elif x*(x-1)/2+(n-x)*(n-x-1)/2==k:
#             #     a=[1]*x
#             #     b=a+[-1]*(n-x)
#             #     print('YES')
#             #     print(*b)
#             #     break
 
#             x-=1
#         else:
#             print('NO')