for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    b.append(a[0])
    flag = 0

    for i in range(1, n):
        if a[i] > b[i-1] or a[i] == 0:
            b.append(a[i]+b[i-1])
        else:
            flag=1
            break

    if flag==1:
        print(-1)
    else:
        print(*b)

# can also be written as

# on line 4
# b = [a[0]]

# on line 11
# else:
#     a = [-1]

# on line 15
# print(*a)