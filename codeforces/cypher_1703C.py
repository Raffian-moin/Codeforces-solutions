test_cases = int(input())

while test_cases:

    wheel_numbers = int(input())

    # final_combination = list(map(int, input().split()))
    final_combination = list(map(int,input().split()))

    number_of_moves, moves = input().split()
    first_wheel_moves = list(map(int,[number_of_moves]))
    first_wheel_moves.append(moves.upper())

    number_of_moves, moves = input().split()
    second_wheel_moves = list(map(int,[number_of_moves]))
    second_wheel_moves.append(moves.upper())

    number_of_moves, moves = input().split()
    third_wheel_moves = list(map(int,[number_of_moves]))
    third_wheel_moves.append(moves.upper())

    count = final_combination[0]
    for index, value in enumerate(first_wheel_moves[1]):
        if 'D' == value:
            if count == 10:
                count = 0
            count = count + 1

            print(count)

    # first_wheel_moves = list(map(input().split()))
    # second_wheel_moves = list(map(input().split()))
    # third_wheel_moves = list(map(input().split()))

    print(wheel_numbers)
    print(final_combination)
    print(first_wheel_moves)
    print(second_wheel_moves)
    print(third_wheel_moves)

    test_cases -= test_cases