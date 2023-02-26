import math
for _ in range(int(input())):
    s = input()
    t = input()

    if len(s)*t != len(t)*s:
        print(-1)
    else:
        print((math.lcm(len(s), len(t))//len(s))*s)


# === another solution using gcd ===

# import math
# for _ in range(int(input())):
#     s = input()
#     t = input()
#     q = math.gcd(len(s), len(t))
#     ss,tt = s * (len(t)//q),t*(len(s)//q)
#     print(ss if ss==tt else -1)

# formula:
# gcd * lcm = a*b 
# gcd = a*(b/gcd) for a 
# gcd = b* (a/gcd) for b