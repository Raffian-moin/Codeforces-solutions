for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    m=a.index(max(a))

    if sorted(a)==a or sorted(a, reverse=True)==a:
        print('YES')
    elif a[:m]==sorted(a[:m]) and a[m+1:]==sorted(a[m+1:], reverse=True):
        print('YES')
    else:
        print('NO')

# can also be written like below in constructive way

# s = 1
# for i in range(1, n):
#     if a[i-1] > a[i]:
#         s = 0
#     elif a[i-1] < a[i] and s == 0:
#         print("NO")
#         break
# else:
#     print("YES")