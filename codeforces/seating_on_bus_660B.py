n, m = list(map(int, input().split()))

total_row = n*2

my_dic = {}

non_window_seat_number = total_row+1

for window_seat in range(1, total_row+1):
    if non_window_seat_number <= m:
        non_window_seat = non_window_seat_number
        non_window_seat_number = non_window_seat_number + 1
    else:
        non_window_seat = None
    if m >= window_seat:
        my_dic[window_seat] = non_window_seat

for key, value in my_dic.items():
    if value != None:
        print(value)
    print(key)

