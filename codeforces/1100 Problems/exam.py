n=int(input())

if n<=2:
    print(1)
    print(1)
elif n==3:
    print(2)
    print(1, 3)
else:
    print(n)
    for number in range(2, n+1, 2):
        print(number, end=" ")

    for number in range(1, n+1, 2):
        print(number, end=" ")