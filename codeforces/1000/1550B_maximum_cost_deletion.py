from itertools import groupby
for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))

    x = input()

    if b >= 0:
        print(n*(a+b))
    else:

        groups = groupby(x)
        result = [(label, sum(1 for _ in group)) for label, group in groups]
        zero = 0
        one = 0
        for i in range(len(result)):
            if result[i][0] == '0':
                zero+= 1
            else:
                one+= 1
        print(n*a+ (min(zero, one)+1)*b)

        # can also be written to find number of groups of 1's and 0's
        # print(n*a+b*(max(k.count('01'),k.count('10'))+1))
