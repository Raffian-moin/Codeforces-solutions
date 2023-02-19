for _ in range(int(input())):
    n, m = list(map(int, input().split()))

    s = input()
    t = input()

    if (s.count('BB')+s.count('RR')+t.count('BB')+t.count('RR') > 1 or s.count('BBB')+s.count('RRR')+t.count('BBB')+t.count('RRR') == 1):
        print('NO')
    elif ((s.count('BB')+s.count('RR')+t.count('BB')+t.count('RR') == 1) and s[n-1] == t[m-1]):
        print('NO')
    else:
        print('YES')


# also possibe answer
# s = input()
# t = input()
# v = s + t[::-1]
# count = v.count("BB") + v.count("RR")
# if count > 1 or "RRR" in v or "BBB" in v: print("NO")
# else:
#     print("YES")

