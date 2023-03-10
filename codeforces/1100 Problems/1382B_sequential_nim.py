for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    i=0
    while(a[i]==1 and i<n-1):
        i+=1

    print('First' if i%2==0 else 'Second')
