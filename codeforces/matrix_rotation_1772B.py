# t = int(input())

# while t:
#     target = 0
#     a = list(map(int,input().split(' ')))
#     b = list(map(int,input().split(' ')))
#     for i in range(4):
#         if a[0] < a[1] and a[0] < b[0] and a[1] < b[1] and b[0] < b[1]:
#             target =1
#             break
#         else:
#             a[0], a[1], b[0], b[1] = b[0], a[0], b[1], a[1]


#     print('YES' if target==1 else 'NO')
#     t = t-1
t=1
for i in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    print(a, b, c, d)
    if (a>b)==(c>d) and (a<c)==(b<d):
        print('YES')
    else:
        print("NO")

