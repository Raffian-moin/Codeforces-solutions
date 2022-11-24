import math
test_cases = int(input())

favorite_numbers = list(map(int, input().split()))

for number in favorite_numbers:
    if number < 15:
        print('NO')
    elif number > 14 and number <21:
        print('YES')
    elif number > 20:
        number_of_dice =  math.floor(number/14)

        if (number_of_dice-1)*14 + 20 >= number:
            remaining_for_last_dice = number - 14*(number_of_dice-1)
        else:
            remaining_for_last_dice = number - (14*(number_of_dice-1))

        if (remaining_for_last_dice <=20 and remaining_for_last_dice >= 15):
            print('YES')
        elif remaining_for_last_dice < 15:
            print('NO')

