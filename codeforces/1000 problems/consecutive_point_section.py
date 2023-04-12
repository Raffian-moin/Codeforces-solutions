for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    two=0
    three=0
    m=0

    for i in range(1, n):
        if a[i]-a[i-1] >3:
            m+=1
        if a[i]-a[i-1]==2:
            two+=1
        if a[i]-a[i-1]==3:
            three+=1

    if m>0 or three>1 or two>2 or (three>0 and two>0):
        print('NO')
    else:
        print('YES')

# can also written in just one line
# print('YES' if a[-1] - a[0] - n  <= 1 else 'NO')
