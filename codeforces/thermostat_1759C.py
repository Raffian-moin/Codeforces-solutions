inputs1 = list(map(int, input().split()))
inputs2 = list(map(int, input().split()))

l = inputs1[0]
r = inputs1[1]
min_change = inputs1[2]
initial_temperature = inputs2[0]
final_temperature = inputs2[1]

if final_temperature - initial_temperature >= min_change and final_temperature - initial_temperature <= r:
    print(1)
elif final_temperature - initial_temperature < min_change:
    