for _ in range(int(input())):

    n = int(input())
    array = list(map(int, input().split()))
    sum = array[0]

    double_negative = False
    positive_negative = False

    for i in range(1, n):
        sum = sum+array[i]
        if array[i] == -1 and array[i-1] == -1:
            double_negative = True
        elif (array[i] == -1 and array[i-1] == 1) or (array[i] == 1 and array[i-1] == -1):
            positive_negative = True

    if double_negative == True:
        print(sum+4)
    elif positive_negative == True:
        print(sum)
    else:
        print(sum-4)
       