n=int(input())
a=list(map(int, input().split()))
b=sorted(a)

if a==b:
    print(0)
else:
    for i in range(1, n):
        if a[i] < a[i-1]:
            if a[i:]==b[:n-i]:
                a[i:]==b[:n-i]
                print(len(a[i:]))
            else:
                print(-1)
            break

# can alos be written as 
# for i in range(1, n):
#     if a[i] < a[i-1]:
#         print(n-i if a[i:]==b[:n-i] else -1)
#         break
# else:
#     print(0)