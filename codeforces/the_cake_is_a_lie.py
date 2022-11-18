test_cases = int(input())

while test_cases:

    inputs = list(map(int,input().split()))
    horizontal_moves = 0
    vertical_moves = 0
    target_x_coordinate = inputs[0]
    target_y_coordinate = inputs[1]
    if (target_x_coordinate != 1):
        horizontal_moves = (target_x_coordinate - 1) * target_y_coordinate
    if (target_y_coordinate != 1):
        vertical_moves = (target_y_coordinate - 1)

    if horizontal_moves + vertical_moves == inputs[2]:
        print('YES')
    else:
        print('NO')
    test_cases-=1