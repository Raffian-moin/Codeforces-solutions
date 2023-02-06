s = input()
s1 = ''
s2 = ''
for index in range(len(s)):
    if s[index] != s[s(len)-1+index]:
        s1 = s[index]+s[s(len)-1+index]
        s1 = s[s(len)-1+index]+s[index]
    else:
        s1 = s1+s[index]+s[index]
        s2 = s2+s[index]+s[index]