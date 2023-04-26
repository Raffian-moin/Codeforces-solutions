for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))


    for i in range(n-1):
        if (a[i] > a[-1] and b[i]>a[-1]) or (a[i]>b[-1] and b[i]>b[-1]) or(a[i]>a[-1] and a[i]>b[-1]) or (b[i]>b[-1] and b[i]>a[-1]):
            print('No')
            break
    else:
        print('Yes')

# another solution
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     for i in range(n):
#         if a[i] > b[i]:
#             a[i], b[i] = b[i], a[i]
#     if a[-1] == max(a) and b[-1] == max(b):
#         print("YES")
#     else:
#         print("NO")