for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    n, m = list(map(int, input().split()))

    if m<n:
        print(min(n//(m+1)*m*a+(n%(m+1))*b, b*n, n//(m+1)*m*a+(n%(m+1))*a))
    else:
        print(min(a*n, b*n))