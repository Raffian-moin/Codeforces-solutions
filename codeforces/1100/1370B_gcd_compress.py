for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    odd = []
    even=[]

    for i in range(n*2):
        if a[i]%2==0:
            even.append(i+1)
        else:
            odd.append(i+1)

    if len(odd)%2==1 and len(even)%2==1:
        odd = odd[:-1]
        even = even[:-1]
    elif len(odd) >=  len(even):
        odd = odd[:len(odd)-2]
    else:
        even = even[:len(even)-2]

    even=even+odd

    for i in range(0, n*2-2, 2):
        print(even[i], even[i+1])