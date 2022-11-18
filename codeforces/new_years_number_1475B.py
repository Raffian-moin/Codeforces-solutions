number = int(input())

def divideBySix(number):
    return number % 6

def divideBySeven(number):
    return number % 7

if number > 6:
    mod = divideBySeven(number)

    if mod < 6 and mod != 0:
        mod = divideBySix(number)
    if mod == 6 and mod != 0 :
        mod = divideBySix(mod)
    # if mod
# print(mod)
if mod == 0:
    print('YES')