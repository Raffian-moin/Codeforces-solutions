for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    mi=min(a)
    min_in=a.index(min(a))
    print(n-1)
    for index in range(n):
        if index==min_in:
            continue

        i, j, x, y = index+1, min_in+1, mi, mi

        if min_in%2!=index%2 and index<min_in:
            x+=1
        elif min_in < index:
            i,j=j,i
            if min_in%2!=index%2:
                y+=1

        print(i, j, x, y)