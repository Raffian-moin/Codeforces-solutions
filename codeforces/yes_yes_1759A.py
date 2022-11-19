import math

test_cases = int(input())
yes = ''
count = 0
while count < test_cases:
    answer = input()

    answer_length = len(answer)

    number_of_yes = math.ceil(answer_length/3)

    for _ in range(number_of_yes+1):
        yes = yes + 'Yes'

    if answer in yes:
        print('YES')
    else:
        print('NO')
    count += 1