for _ in range(int(input())):
    n, k = list(map(int, input().split()))

    if n <= k:
        print(k//n if k%n == 0 else (k//n)+1)
    else:
        print('1' if n%k==0 else '2')