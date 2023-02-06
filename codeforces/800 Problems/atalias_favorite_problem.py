n = int(input())

while n:
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    length = int(input())

    string = input()

    max = 1

    for ch in string:
        number = alphabets.index(ch)+1
        if number >= max:
            max = number
    n = n -1
    
    print(max)