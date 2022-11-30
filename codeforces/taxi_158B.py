# n = int(input())
# l = list(map(int, input().split()))
# count = 1
# sum = 0

# for i in range(n):
#     if sum+l[i] <=4:
#         sum = sum+l[i]
#     else:
#         count = count+1
#         sum = 0

# print(count)

input()
a,b,c,d=map(input().count,('1','2','3','4'))
print(a)
print(b)
print(d+c+(b*2+max(0,a-c)+3)//4)
