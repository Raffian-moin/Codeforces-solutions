for _ in range(int(input())):
    a,b,c=list(map(int, input().split()))
    a,b,c=sorted([a,b,c])
    print(max(0, c-b-2+ c-a-2+ b-a))