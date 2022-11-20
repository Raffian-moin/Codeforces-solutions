import math
test_cases = int(input())

favorite_numbers = list(map(int, input().split()))

for number in favorite_numbers:
    if number < 15:
        print('NO')
    else:
        number_of_dice =  math.ceil(number/14)
        if (14 * number_of_dice) + 1 <= number:
            number_of_dice =  number_of_dice
        else:
            number_of_dice =  math.floor(number/14)

        remaining_for_last_dice = 14*(number_of_dice - 1)

        if (number-remaining_for_last_dice <=20 and number-remaining_for_last_dice >= 15):
            print('YES')
        else:
            print('NO')

