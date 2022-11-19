import math
test_cases = int(input())

count = 0
while count < test_cases:
    old_price, multiply_number = list(map(int, input().split()))

    if multiply_number < 10:
        print(old_price * multiply_number)
    else:
        if (math.floor(multiply_number/10)+.5) < multiply_number/10 and old_price % 2 == 0: 
            print(int(old_price * (math.floor(multiply_number/10)+.5)*10))
        else :
            print(int(old_price * (math.floor(multiply_number/10))*10))
    count += 1
