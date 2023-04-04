for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    l=len(a)
    a.sort()
    s=sum(a[:l-1])
    m=a[-1]

    
    if a[-2]==sum(a[:l-2]):
        a.remove(a[-1])
        a.remove(a[-1])
        print(*a)
    elif s-m in a[:l-1]:
        a.remove(s-m)
        a.remove(a[-1])
        print(*a)
    else:
        print(-1)

# can also be done without getting len(a)

# if sum(a[:-2]) == a[-2]:
#     print(*a[:-2])
# elif s-m in a[:-1]:
#     a.remove(s-m)
#     print(*a[:-1])
# else:print(-1)