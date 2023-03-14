for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    print(10**(a-1), int('1'*(b-(c-1))+'0'*(c-1)))