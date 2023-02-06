t =int(input())

while t:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    target_string = input()
    nm = int(input())
    new_string = ''

    count = 0

    for i in range(len(target_string)):
        if alphabets.find(target_string[i])+1 <= nm and count+alphabets.find(target_string[i])+1 <= nm:
            new_string+=target_string[i]
            count = count+alphabets.find(target_string[i])+1

    print(new_string)
    t = t-1