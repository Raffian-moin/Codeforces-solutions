vowels = ["A", "E", "I", "O", "U","Y"]
 
s = input()
c = 1
jump = 1
for ch in s:
    if ch not in vowels:
        c = c+1
        jump = max(c, jump)
    else:
        c = 1
 
print(jump)