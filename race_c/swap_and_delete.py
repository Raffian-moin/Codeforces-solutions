for _ in range(int(input())):
    s = input()

    ones = s.count("1")
    zeroes = len(s) - ones

    for ch in s:
        if ch == '1' and zeroes > 0:
            zeroes -=1
        elif ch == '0' and ones > 0:
            ones -=1
        else:
            break

    print(ones + zeroes)
