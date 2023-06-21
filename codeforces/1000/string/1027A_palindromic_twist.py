for _ in range(int(input())):
    n = int(input())
    s = input()

    for i in range(n//2):
        if s[i] != s[n-1-i] and abs(ord(s[i]) - ord(s[n-1-i])) != 2:
            print('NO')
            break
    else:
        print('YES')


# if distance between the letters are 0 or 2 it can be transform to palindrome
# so condition can be 
# if diff != 0 or diff !=2