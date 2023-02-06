time = input()

hour = int(time.split(':')[0])
min = int(time.split(':')[1])

def makePalindrome(hour, min=None):
    q, mod = divmod(hour, 10)
    palindrome_minute = mod*10+q
    if palindrome_minute>60:
        return makePalindrome(hour+1, palindrome_minute)
    elif palindrome_minute >= min:
        return makePalindrome(hour+1)
    elif min == None:
        return [hour,palindrome_minute]


if hour+1 != 24:
    hour, minute = makePalindrome(hour, min)

    print(f"{hour:02d}:{minute:02d}")
else:
    print("00:00")